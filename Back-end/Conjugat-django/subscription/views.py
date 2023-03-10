
from coinbase_commerce.client import Client
from django.conf import settings
from django.urls import reverse
from .encryption import decrypt, encrypt

from .models import UserProfile, PaymentMethod
from .paypal import show_sub_details, suspend_sub, activate_sub
import stripe

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


''' Setup '''
def does_subscriber_exist(request):
    try:
        subscriber = UserProfile.objects.get(user=request.user)
    except:
        subscriber = None
    return subscriber

def is_user_subscribed(subscriber):
    if subscriber:
        subscribed = subscriber.subscribed
    else:
        subscribed = False
    return subscribed

def does_trial_exist(subscriber):
    if subscriber:
        trial = subscriber.trial
    else:
        trial = True
    return trial

def obtain_method(subscriber):
    if subscriber:
        method = str(subscriber.method)
    else:
        method = None
    return method

# Instead of making an expensive call to postgres I am using a function instead.
def payment_method(method):
    if method == 'Stripe':
        return 1
    elif method == 'Paypal':
        return 2
    elif method == 'Coinbase':
        return 3

def save_subscriber(request, method, subscriber, subscriber_id=None, customer_id=None):
    if not subscriber:
        subscriber = UserProfile.objects.create(user=request.user, method_id=payment_method(method))
    subscriber.method_id=payment_method(method)
    # Reset the subscription and customer ids
    subscriber.subscription_id = None
    subscriber.customer_id = None
    if customer_id:
        subscriber.customer_id = encrypt(customer_id)
    if subscriber_id:
        subscriber.subscription_id = encrypt(subscriber_id)
    subscriber.save()




''' Process '''
stripe.api_key = settings.STRIPE_SECRET_KEY

def build_stripe_checkout(request, subscriber, customer, success_url, cancel_url):
    prices = stripe.Price.list(
            lookup_keys=[request.data.get('lookup_key')],
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

def build_coinbase_checkout(subscriber, success_url, cancel_url):
    client = Client(api_key=settings.COINBASE_COMMERCE_API_KEY)

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

from .serializers import ProcessSerializer
@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def processView(request):
    subscriber = does_subscriber_exist(request)
    if request.method == "GET":
        serializer = ProcessSerializer(subscriber)
        return Response(data=serializer.data,
                            status=status.HTTP_200_OK)

    if request.method == "POST":
        success_url = request.data.get("success_url")
        cancel_url = request.data.get("cancel_url")
        if request.data.get('method') == 'Stripe':
            if not subscriber or subscriber.subscribed == False:
                customer = stripe.Customer.create()
                checkout_session = build_stripe_checkout(request, subscriber, customer, success_url, cancel_url)
                save_subscriber(request, 'Stripe', subscriber, customer_id = customer.id)
                return Response({'url':checkout_session.url},
                                status=status.HTTP_200_OK)

        if request.data.get('method') == 'Paypal':
            subscriptionID = request.data.get('subscriptionID')
            save_subscriber(request, 'Paypal', subscriber, subscriber_id=subscriptionID)
            return Response(status=status.HTTP_200_OK)

        if request.data.get('method') == 'Coinbase':
            if not subscriber or subscriber.subscribed == False:
                charge = build_coinbase_checkout(subscriber, success_url, cancel_url)
                subscriber_id = charge.hosted_url.rsplit('/', 1)[1]
                save_subscriber(request, 'Coinbase', subscriber, subscriber_id=subscriber_id)
                return Response({'url':charge.hosted_url},
                                status=status.HTTP_200_OK)







'''Success'''
def build_stripe_portal(request, subscriber, return_url=None):
    if not return_url:
        return_url = request.build_absolute_uri(reverse('subscription:options'))
    customer = decrypt(subscriber.customer_id)
    portalSession = stripe.billing_portal.Session.create(
                    customer=customer,
                    return_url=return_url,
    )
    return portalSession


from .serializers import SuccessSerializer
@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def successView(request):
    subscriber = does_subscriber_exist(request)
    method = obtain_method(subscriber)
    
    if request.method == "GET":
        subscriber.charge = None
        subscriber.status = None
        if method == 'Coinbase':
            client = Client(api_key=settings.COINBASE_COMMERCE_API_KEY)
            charge_id = decrypt(subscriber.subscription_id)
            charge = client.charge.retrieve(charge_id)
            subscriber.charge = charge.hosted_url
        
        if method == 'Paypal':
            subscription_id = decrypt(subscriber.subscription_id)
            details = show_sub_details(subscription_id)
            subscriber.status = details['status']

        serializer = SuccessSerializer(subscriber)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    if request.method == "POST":
        return_url = request.data.get('return_url')
        if method == 'Stripe':
            stripe_portal = build_stripe_portal(request, subscriber, return_url)
            return Response({'url':stripe_portal.url},
                            status=status.HTTP_200_OK)
        
        if method == 'Paypal':
            action = request.data.get('action')
            subscription_id = decrypt(subscriber.subscription_id)
            if action == 'Stop':
                suspend_sub(subscription_id)
                success = 'subscription has been paused'
                return Response({'success':success},
                            status=status.HTTP_200_OK)
            
            elif action == 'Re-start':
                activate_sub(subscription_id)
                success = 'subscription has been re-started'
                return Response({'success':success},
                            status=status.HTTP_200_OK)

        else:
            error = 'Invalid method'
            return Response({'error':error},
                            status=status.HTTP_404_NOT_FOUND)