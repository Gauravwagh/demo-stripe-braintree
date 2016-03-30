from django.shortcuts import render

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
# Create your views here.
from django.contrib import messages

import stripe
from utils import payment_data
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required


@login_required
@csrf_exempt
def home(request):
    client_token = payment_data(request.user)
    # Post request for creating the stripe Charge
    if request.method == "POST":
        # secret key remember to change this to live secret key in production
        stripe.api_key = "sk_test_SpkSUcTvR8wtUJW8rTgExcz3"

        # Get the credit card details submitted by the form
        token = request.POST['stripeToken']

        # Create the charge on Stripe's servers - this will charge the user's card
        try:
          charge = stripe.Charge.create(
              amount=2000, # amount in cents, again
              currency="usd",
              source=token,
              description="Example charge"
          )
          messages.info(request, "Payment is successful")
        except stripe.error.CardError, e:
          # The card has been declined
          print e.message
          pass
    return render(request, 'home/home.html', {"client_token":client_token})