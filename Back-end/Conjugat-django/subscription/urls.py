from django.urls import path
from . import views
from . import webhooks

app_name = "subscription"
urlpatterns = [
    path('', views.GetRoutes.as_view(), name='get_routes'),

    path('retrieve-status/', views.RetrieveStatus.as_view(), name='retrieve_status'),
    path('new-stripe-customer/', views.NewStripeCustomer.as_view(), name='new_stripe_customer'),
    path('new-paypal-customer/', views.NewPaypalCustomer.as_view(), name='new_paypal_customer'),
    path('new-coinbase-customer/', views.NewCoinbaseCustomer.as_view(), name='new_coinbase_customer'),
    path('process/', views.processView, name='options'),
    path('success/', views.successView, name='success'),

    path('stripe-webhooks/', webhooks.stripe_webhooks, name="stripe_webhooks"),
    path('paypal-webhooks/', webhooks.paypal_webhooks, name='paypal_webhooks'),
    path('coinbase-webhooks/', webhooks.coinbase_webhooks, name='coinbase_webhooks'),   
]