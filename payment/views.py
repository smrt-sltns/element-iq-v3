import json
import os
import stripe

from django.shortcuts import render, redirect
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

from account.models import User
from .models import TokenOffer
from .utils import create_checkout_session
from account.auth import admin_only

stripe.api_key = settings.STRIPE_API_KEY

@csrf_exempt
@login_required
@admin_only
def list_offers(request):

    if request.method == "POST":
        data = json.loads(request.body)
        price_id = data["priceId"]
        username = data["username"]
        email = data["email"]
        redirect_url = create_checkout_session(price_id, username, email)
        return JsonResponse({"redirect_url": redirect_url})

    context = {}
    token_offers = TokenOffer.objects.all()

    context["token_offers"] = [
        {
            "name": o.name,
            "price": o.price,
            "priceId": o.price_id,
        }
    for o in token_offers ]

    context["STRIPE_PUBLISHABLE_KEY"] = settings.STRIPE_PUBLISHABLE_KEY

    return render(request, "payment/list-offers.html", context)

@login_required
def checkout_session(request):

    id = request.GET.get('session_id')
    print(id)
    checkout_session = stripe.checkout.Session.retrieve(id)
    if checkout_session != None:
        user = request.user
        user.stripe_session = checkout_session['id']
        cents = checkout_session['amount_total']

        user.token += int(cents/3)
        user.save()
        print(user.email+' bought ' + str(int(cents/3)) + ' tokens!')

    return redirect("image_apis:generate")




"""

def create_checkout_session(request):
    data = json.loads(request.data)

    try:
        # See https://stripe.com/docs/api/checkout/sessions/create
        # for additional parameters to pass.
        # {CHECKOUT_SESSION_ID} is a string literal; do not change it!
        # the actual Session ID is returned in the query parameter when your customer
        # is redirected to the success page.
            # payment_method_types=["card"],
        checkout_session = stripe.checkout.Session.create(
            success_url=request.url_root+"checkout-session?session_id={CHECKOUT_SESSION_ID}",
            cancel_url=request.url_root+"dashboard",
            mode="payment",
            line_items=[
                {
                    "price": data['priceId'],
                    # For metered billing, do not pass quantity
                    "quantity": 1
                }
            ],
        )
        return jsonify({'sessionId': checkout_session['id']})
    except Exception as e:
        return jsonify({'error': {'message': str(e)}}), 400

def checkout_session(request):
    id = request.args.get('session_id')
    print(id)
    checkout_session = stripe.checkout.Session.retrieve(id)
    if checkout_session != None:
        user = request.user
        user.stripe_session = checkout_session['id']
        cents = checkout_session['amount_total']
        user.token_amount += int(cents/5)
        user.save()
        print(user.email+' bought ' + str(int(cents/5)) + 'tokens!')

    return redirect(url_for("main.index"))

@blueprint.route('/customer-portal', methods=['GET'])
def customer_portal():
    # For demonstration purposes, we're using the Checkout session to retrieve the customer ID.
    # Typically this is stored alongside the authenticated user in your database.
    user = User.query.filter_by(id=current_user.id).first()
    checkout_session_id = user.stripe_session
   
    print(user.name)
    print(user.stripe_session)
    print(user.email)
    checkout_session = stripe.checkout.Session.retrieve(checkout_session_id)

    # This is the URL to which the customer will be redirected after they are
    # done managing their billing with the portal.
    return_url = request.url_root

    session = stripe.billing_portal.Session.create(
        customer=checkout_session.customer,
        return_url=return_url)
    print(return_url)
    return jsonify({'url': session.url})

@blueprint.route('/webhook', methods=['POST'])
def webhook_received():
    weaccountbhook_secret = settings.STRIPE_WEBHOOK_SECRET
    request_data = json.loads(request.data)
    user = User.query.filter_by(id=current_user.id).first()
    if webhook_secret:
        # Retrieve the event by verifying the signature using the raw body and secret if webhook signing is configured.
        signature = request.headers.get('stripe-signature')
        try:
            event = stripe.Webhook.construct_event(
                payload=request.data, sig_header=signature, secret=webhook_secret)
            data = event['data']
        except Exception as e:
            return e
        # Get the type of webhook event sent - used to check the status of PaymentIntents.
        event_type = event['type']
    else:
        data = request_data['data']
        event_type = request_data['type']
    data_object = data['object']

    if event_type == 'checkout.session.completed':
        # Payment is successful and the subscription is created.
        # You should provision the subscription.
        
        print(data)
    elif event_type == 'invoice.paid':
        # Continue to provision the subscription as payments continue to be made.
        # Store the status in your database and check when a user accesses your service.
        # This approach helps you avoid hitting rate limits.
        print(data)
    elif event_type == 'invoice.payment_failed':
        # The payment failed or the customer does not have a valid payment method.
        # The subscription becomes past_due. Notify your customer and send them to the
        # customer portal to update their payment information.
        print(data)
    else:
        print('Unhandled event type {}'.format(event_type))

        
"""
