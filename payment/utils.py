
import stripe

from django.conf import settings

stripe.api_key = settings.STRIPE_API_KEY


PAYMENT_BASE_URL = "http://localhost:8000/payment/"

def create_checkout_session(price_id, username, email):
    customer = stripe.Customer.create(
        name=username,
        email=email,
    )

    checkout_session = stripe.checkout.Session.create(
        success_url=PAYMENT_BASE_URL+"checkout-session?session_id={CHECKOUT_SESSION_ID}",
        cancel_url=PAYMENT_BASE_URL,
        mode="payment",
        line_items=[
            {
                "price": price_id,
                "quantity": 1
            }
        ],
        customer=customer
    )


    # session = stripe.billing_portal.Session.create(
    #     customer=checkout_session.customer,
    #     return_url=BASE_URL+"/payment/"
    # )
    
    return checkout_session.url



