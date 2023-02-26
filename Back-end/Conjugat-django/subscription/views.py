from .encryption import decrypt, encrypt
from .models import UserProfile, PaymentMethod
from .paypal import show_sub_details, suspend_sub, activate_sub
from coinbase_commerce.client import Client
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
import json
import stripe


from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes


''' Setup '''
def does_subscriber_exist(request):
    try:
        subscriber = get_object_or_404(UserProfile, user=request.user)
    except:
        subscriber = None
    return subscriber

def obtain_method(subscriber):
    if subscriber:
        method = str(subscriber.method)
    else:
        method = None
    return method


def payment_method(method):
    if method == 'Stripe':
        return 1
    elif method == 'Paypal':
        return 2
    elif method == 'Coinbase':
        return 3

# Redirect urls for if the subscriber has an active subscription
def url_if_subscribed(subscriber):
    print(subscriber)
    if str(subscriber.method) == 'Stripe':
        return 'subscription:stripe_success'
    elif str(subscriber.method) == 'Paypal':
        return 'subscription:paypal_success'
    elif str(subscriber.method) == 'Coinbase':
        return 'subscription:coinbase_success'
    else:
        return 'home'

def url_if_not_subscribed(subscriber):
    if not subscriber:
        return 'subscription:options'
    if str(subscriber.method) == 'Stripe':
        return 'subscription:stripe_process'
    elif str(subscriber.method) == 'Paypal':
        return 'subscription:paypal_process'
    elif str(subscriber.method) == 'Coinbase':
        return 'subscription:coinbase_process'

def save_subscriber(request, method, subscriber, subscriber_id=None, customer_id=None):
    if not subscriber:
        subscriber = UserProfile.objects.create(user=request.user, method_id=payment_method(method))
        # subscriber.save()
    subscriber.method_id=payment_method(method)
    if customer_id:
        subscriber.customer_id = encrypt(customer_id)
    if subscriber_id:
        subscriber.subscription_id = encrypt(subscriber_id)
    subscriber.save()





''' Options '''
# Page to list the payment options
@login_required
def options(request):
    subscriber = does_subscriber_exist(request)
    if not subscriber or subscriber.subscribed != True:
        return render(request, 'subscription/options.html')
    else:
        return redirect(url_if_subscribed(subscriber))




'''Success'''
@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def successView(request):
    subscriber = does_subscriber_exist(request)
    method = obtain_method(subscriber)
    
    if request.method == "GET":
        if subscriber:
            subscribed = subscriber.subscribed
        else:
            subscribed = False

        context = {'subscribed':subscribed, 'method':method}
        print(context)
        return Response(data=context, status=status.HTTP_200_OK)

    if request.method == "POST":
        return_url = request.data.get('return_url')
        if method == 'Stripe':
            stripe_portal = build_stripe_portal(request, subscriber, return_url)
            return Response({'url':stripe_portal.url},
                            status=status.HTTP_200_OK)


@login_required
def stripe_success(request):
    subscriber = does_subscriber_exist(request)
    if subscriber:
        if subscriber.subscribed == True:
            if str(subscriber.method) == 'Stripe':
                if request.method == 'POST':
                    stripe_portal = build_stripe_portal(request, subscriber)
                    print(stripe_portal.url)
                    return redirect(stripe_portal.url, code=303)
                else:
                    return render(request, 'subscription/stripe/success.html')
            else:
                return redirect(url_if_subscribed(subscriber))
    return redirect(url_if_not_subscribed(subscriber))


''' Stripe '''
stripe.api_key = settings.STRIPE_SECRET_KEY

def build_stripe_checkout(request, subscriber, customer):
    success_url = request.build_absolute_uri(reverse('subscription:stripe_success'))
    cancel_url = request.build_absolute_uri(reverse('subscription:stripe_cancelled'))

    prices = stripe.Price.list(
            lookup_keys=[request.POST.get('lookup_key')],
            expand=['data.product']
    )
    line_items=[
                {
                    'price': prices.data[0].id,
                    'quantity': 1,
                },
    ]

    checkout_kwargs = {
        'line_items' : line_items,
        'customer':customer,
        'mode':'subscription',
        'success_url':success_url,
        'cancel_url':cancel_url,
    }
    if not subscriber or subscriber.trial == True:
        checkout_kwargs['subscription_data'] = {'trial_period_days':7}

    checkout_session = stripe.checkout.Session.create(**checkout_kwargs)
    return checkout_session



def build_stripe_portal(request, subscriber, return_url=None):
    if not return_url:
        return_url = request.build_absolute_uri(reverse('subscription:stripe_success'))
    customer = decrypt(subscriber.customer_id)
    portalSession = stripe.billing_portal.Session.create(
                    customer=customer,
                    return_url=return_url,
    )
    return portalSession



@login_required
def stripe_process(request):
    subscriber = does_subscriber_exist(request)
    if not subscriber or subscriber.subscribed == False:
        if request.method == 'POST':
            customer = stripe.Customer.create()
            checkout_session = build_stripe_checkout(request, subscriber, customer)
            save_subscriber(request, 'Stripe', subscriber, customer_id = customer.id)
            return redirect(checkout_session.url, code=303)

        else:
            return render(request, 'subscription/stripe/process.html')

    else:
        return redirect(url_if_subscribed(subscriber))







@login_required
def stripe_cancelled(request):
    subscriber = does_subscriber_exist(request)
    if not subscriber or subscriber.subscribed == False:
        return render(request, 'subscription/stripe/cancel.html')
    else:
        return redirect(url_if_subscribed(subscriber))










''' Paypal '''
def do_paypal_details_exist(subscriber):
    try:
        sub_id = decrypt(subscriber.subscription_id)
        details = show_sub_details(sub_id)['status']
    except:
        details = None
    return details



@login_required
def paypal_process(request):
    subscriber = does_subscriber_exist(request)
    client_id = settings.PAYPAL_CLIENT_ID
    context = {'trial':True, 'client_id':client_id}
    if subscriber:
        context = {'trial':subscriber.trial, 'client_id':client_id}

    if not subscriber or subscriber.subscribed == False:
        return render(request, 'subscription/paypal/process.html', context)

    else:
        return redirect(url_if_subscribed(subscriber))



def does_json_exist(request):
    try:
        body = json.loads(request.body)
    except:
        body = None
    return body



@login_required
def paypal_subscribe(request):
    subscriber = does_subscriber_exist(request)
    body = does_json_exist(request)
    if body:
        if request.method == 'POST':
            subscriber_id = body['subscriptionID']
            save_subscriber(request, 'Paypal', subscriber, subscriber_id=subscriber_id)
            return redirect('subscription:paypal_success')
    else:
        if not subscriber:
            return redirect(url_if_not_subscribed(subscriber))
        else:
            return redirect(url_if_subscribed(subscriber))



def paypal_success(request):
    subscriber = does_subscriber_exist(request)

    if request.method == 'POST':
        sub_id = decrypt(subscriber.subscription_id)
        if request.POST.get('Stop'):
            suspend_sub(sub_id)
            return redirect('subscription:paypal_success')

        elif request.POST.get('Re-start'):
            activate_sub(sub_id)
            return redirect('subscription:paypal_success')

    else:
        if not subscriber or subscriber.subscribed == False:
            return redirect(url_if_not_subscribed(subscriber))
        else:
            if str(subscriber.method) == 'Paypal':
                sub_id = decrypt(subscriber.subscription_id)
                details = show_sub_details(sub_id)
                context = {'id':subscriber.subscription_id, 'status': details['status']}
                return render(request, 'subscription/paypal/subscribed.html', context)
            else:
                return redirect(url_if_subscribed(subscriber))










''' Coinbase '''
def build_coinbase_checkout(request, subscriber):
    client = Client(api_key=settings.COINBASE_COMMERCE_API_KEY)

    success_url = request.build_absolute_uri(reverse('subscription:coinbase_success'))
    cancel_url = request.build_absolute_uri(reverse('subscription:coinbase_process'))

    checkout_kwargs = {
        'name':'Conjugat Premium',
        'local_price': {
            'currency':'GBP'
        },
        'pricing_type':'fixed_price',
        'rediret_url':success_url,
        'cancel_url':cancel_url,
    }
    if not subscriber or subscriber.trial == True:
        checkout_kwargs['description'] = '1 Week of conjugat Premium'
        checkout_kwargs['local_price']['amount'] = '0.01'
    else:
        checkout_kwargs['description'] = '1 Month of conjugat Premium'
        checkout_kwargs['local_price']['amount'] = '2.50'
    
    charge = client.charge.create(**checkout_kwargs)

    return charge


@login_required
def coinbase_process(request):
    subscriber = does_subscriber_exist(request)

    if not subscriber or subscriber.subscribed == False:
        charge = build_coinbase_checkout(request, subscriber)
        #subscriber_id = charge.hosted_url.rsplit('/', 1)[1]
        subscriber_id = charge.hosted_url.rsplit('/', 1)[1]
        save_subscriber(request, 'Coinbase', subscriber, subscriber_id=subscriber_id)

        context = {'charge':charge}
        return render(request, 'subscription/coinbase/process.html', context)

    else:
        return redirect(url_if_subscribed(subscriber))



@login_required
def coinbase_success(request):
    subscriber = does_subscriber_exist(request)        
    if subscriber:
        if subscriber.subscribed == True:
            print(subscriber.method)
            if str(subscriber.method) == 'Coinbase':
                charge_id = decrypt(subscriber.subscription_id)
                client = Client(api_key=settings.COINBASE_COMMERCE_API_KEY)
                charge = client.charge.retrieve(charge_id)
                context = {'charge':charge}
                return render(request, 'subscription/coinbase/success.html', context)
            else:
                return redirect(url_if_subscribed(subscriber))
    return redirect(url_if_not_subscribed(subscriber))



@login_required
def coinbase_cancelled(request):
    subscriber = does_subscriber_exist(request)

    if not subscriber or subscriber.subscribed == False:
        return render(request, 'subscription/coinbase/cancelled.html')
    else:
        return redirect(url_if_subscribed(subscriber))