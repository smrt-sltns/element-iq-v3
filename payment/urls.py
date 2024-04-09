
from django.urls import path
from . import views

app_name = 'payment'
urlpatterns = [
    path('', views.list_offers, name='list-offers'),
    path('checkout-session/', views.checkout_session, name='checkout-session'),
]
