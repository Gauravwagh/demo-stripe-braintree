__author__ = 'gaurav'

import braintree

from billing.models import UserMerchantId
import settings


braintree.Configuration.configure(braintree.Environment.Sandbox,
                                  merchant_id=settings.BRAINTREE_MERCHANT_ID,
                                  public_key=settings.BRAINTREE_PUBLIC_KEY,
                                  private_key=settings.BRAINTREE_PRIVATE_KEY)


def new_user_receiver( instance, *args, **kwargs):
    try:
        merchant_obj = UserMerchantId.objects.get(user=instance)
    except:
        new_customer_result = braintree.Customer.create({
                "first_name": instance.first_name,
                "last_name": instance.last_name,
                "email": instance.email,
            })
        if new_customer_result.is_success:
            merchant_obj, created = UserMerchantId.objects.get_or_create(user=instance)
            merchant_obj.customer_id = new_customer_result.customer.id
            merchant_obj.save()
            print """Customer created with id = {0}""".format(new_customer_result.customer.id)
        else:
            print "Error: {0}".format(new_customer_result.message)



def payment_data(user):

    # checking user is created or not if not create one
    new_user_receiver(user)
    try:
        merchant_obj = UserMerchantId.objects.get(user=user)
        merchant_customer_id = merchant_obj.customer_id
        print merchant_customer_id
        client_token = braintree.ClientToken.generate({
				"customer_id": merchant_customer_id
			})
        print client_token
    except:
        client_token = None
    print merchant_obj
    print client_token
    return client_token