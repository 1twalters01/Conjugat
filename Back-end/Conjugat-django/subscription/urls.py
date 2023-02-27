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




    path('options/', views.options, name='options'),
    path('paypal-process/', views.paypal_process, name='paypal_process'),
    path('paypal-subscribe/', views.paypal_subscribe, name='paypal_subscribe'),
    path('paypal-success/', views.paypal_success, name='paypal_success'),
    

    
]