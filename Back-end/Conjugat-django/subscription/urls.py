from django.urls import path
from . import views
from . import webhooks

app_name = "subscription"
urlpatterns = [
    path('process/', views.processView, name='options'),
    path('success/', views.successView, name='success'),

    path('stripe-webhooks/', webhooks.stripe_webhooks, name="stripe_webhooks"),
    path('paypal-webhooks/', webhooks.paypal_webhooks, name='paypal_webhooks'),
    path('coinbase-webhooks/', webhooks.coinbase_webhooks, name='coinbase_webhooks'),   
]