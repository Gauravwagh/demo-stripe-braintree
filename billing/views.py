from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.

from billing.models import Membership, Transaction, UserMerchantId
from billing.signals import membership_dates_update
from billing.forms import PlanForm

import braintree

braintree.Configuration.configure(braintree.Environment.Sandbox,
                                  merchant_id=settings.BRAINTREE_MERCHANT_ID,
                                  public_key=settings.BRAINTREE_PUBLIC_KEY,
                                  private_key=settings.BRAINTREE_PRIVATE_KEY)


@login_required
def upgrade(request):
    if request.user.is_authenticated():
        if request.method == "POST":
            client_token = request.POST['token']

            try:
                merchant_obj = UserMerchantId.objects.get(user=request.user)
            except:
                messages.error(request, "There was an error with your account. Please contact us.")
                return redirect("contact_us")
            merchant_customer_id = merchant_obj.customer_id
            nonce = request.POST.get("payment_method_nonce", None)
            print "Getting nonce"
            print nonce
            if nonce is None:
                messages.error(request, "An error occued, please try again")
                return redirect("account_upgrade")
            else:
                payment_method_result = braintree.Transaction.sale({
                    "customer_id": merchant_customer_id,
                    "amount": 200,
                    "options": {
                        "submit_for_settlement": True
                    }
                })
                # print dir(payment_method_result.transaction)
                # print payment_method_result
                # print payment_method_result.transaction
                if not payment_method_result.is_success:
                    messages.error(request, "An error occured: %s" % (payment_method_result.message))
                    return redirect("/home/")

                try:
                    the_token = payment_method_result.transaction.credit_card['token']
                    print "getting token"
                    print the_token
                    result = braintree.PaymentMethod.delete(the_token)
                    print result.is_success
                except:
                    pass
                current_sub_id = merchant_obj.subscription_id
                current_plan_id = merchant_obj.plan_id
                did_create_sub = False
                did_update_sub = False
                trans_success = False
                trans_timestamp = None

                membership_instance, created = Membership.objects.get_or_create(user=request.user)
                new_tran, created = Transaction.objects.get_or_create(user=request.user,
                                                                      transaction_id=payment_method_result.transaction.id,
                                                                      amount=payment_method_result.transaction.amount,
                                                                      success=True,
                                                                      transaction_status=payment_method_result.transaction.status)
                try:
                    new_tran.order_id = payment_method_result.transaction.credit_card['token']
                    new_tran.card_type = payment_method_result.transaction.credit_card['card_type']
                    new_tran.last_four = payment_method_result.transaction.credit_card['last_4']
                    new_tran.save()
                except:
                    pass
                trans_success = False
                trans_timestamp = None
                if created:
                    trans_timestamp = new_tran.timestamp
                    trans_success = new_tran.success

                membership_dates_update.send(membership_instance, new_date_start=trans_timestamp)
                sub_id = request.user.usermerchantid.subscription_id
                print ">>>>>>", sub_id
                if sub_id:
                    result = braintree.Subscription.cancel(sub_id)
                    if result.is_success:
                        request.user.usermerchantid.subscription_id = None
                        request.user.usermerchantid.save()
                messages.info(request, "Payment is successful")
                return redirect("/home/")
            context = {"client_token": client_token}
        return redirect('/home/')



