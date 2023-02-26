from django.urls import path
from . import views
from . import webhooks

app_name = "subscription"
urlpatterns = [
    path('success/', views.successView, name='success'),



    path('options/', views.options, name='options'),

    path('stripe-process/', views.stripe_process, name='stripe_process'),
    path('stripe-success/', views.stripe_success, name='stripe_success'),
    path('stripe-cancelled/', views.stripe_cancelled, name='stripe_cancelled'),
    path('stripe-webhooks/', webhooks.stripe_webhooks, name="stripe_webhooks"),

    path('paypal-process/', views.paypal_process, name='paypal_process'),
    path('paypal-subscribe/', views.paypal_subscribe, name='paypal_subscribe'),
    path('paypal-success/', views.paypal_success, name='paypal_success'),
    path('paypal-webhooks/', webhooks.paypal_webhooks, name='paypal_webhooks'),

    path('coinbase-process/', views.coinbase_process, name='coinbase_process'),
    path('coinbase-success/', views.coinbase_success, name='coinbase_success'),
    path('coinbase-cancelled/', views.coinbase_cancelled, name='coinbase_cancelled'),
    path('coinbase-webhooks/', webhooks.coinbase_webhooks, name='coinbase_webhooks'),
]