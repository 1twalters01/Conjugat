
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
from .serializers import ProcessSerializer



from django.contrib.auth.models import User
from rest_framework import status, permissions
from rest_framework.authentication import SessionAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView
# from .serializers import
from .validations import *


from .serializers import RetrieveStatusSerializer, NewStripeCustomerSerializer, \
    NewCoinbaseCustomerSerializer, NewPaypalCustomerSerializer

''' Routes '''
class GetRoutes(APIView):
    def get(self, request):
        routes = [
            {
                'Endpoint': '/process/',
                'method': 'POST',
                'body': {'body': ""},
                'description': 'Post data and retrieve payment details'
            },
            {
                'Endpoint': '/success/',
                'method': 'POST',
                'body': {'body': ""},
                'description': 'Unsubscribes to the newsletter'
            },
        ]
        return Response(routes)

''' Setup '''
def does_subscriber_exist(request):
    try:
        subscriber = UserProfile.objects.get(user=request.user)
    except:
        subscriber = UserProfile.objects.create(user=request.user, method_id=payment_method('None'))
        subscriber.save()
    return subscriber

def is_user_subscribed(request, subscriber):
    if subscriber:
        subscribed = subscriber.subscribed
    else:
        subscriber = UserProfile.objects.create(user=request.user, method_id=payment_method('None'))
        subscriber.save()
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
    elif method == 'None':
        return 4

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
            lookup_keys=['Conjugat Premium'],
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
        checkout_kwargs['local_price']['amount'] = '3.00'
    
    charge = client.charge.create(**checkout_kwargs)
    return charge


class RetrieveStatus(APIView):
    permission_classes = (permissions.AllowAny,)
    # authentication_classes = (SessionAuthentication,)
    def post(self, request):
        data = request.data
        validated_return_urls = validate_return_urls(data)
        if validated_return_urls[0] == False:
            return Response(data=validated_return_urls[1], status=validated_return_urls[2])

        context = {'user': request.user}
        serializer = RetrieveStatusSerializer(data=data, context=context)
        if serializer.is_valid(raise_exception=True):
            response = serializer.retrieve_status(data)
            if response[1] == True:
                return Response(data=response[0], status=status.HTTP_200_OK)
            return Response({'error':response[0]}, status=response[2])

class NewStripeCustomer(APIView):
    permission_classes = (permissions.AllowAny,)
    # authentication_classes = (SessionAuthentication,)
    def post(self, request):
        data = request.data
        validated_customer_id = validate_customer_id(data)
        if validated_customer_id[0] == False:
            return Response(data=validated_customer_id[1], status=validated_customer_id[2])

        context = {'user': request.user}
        serializer = NewStripeCustomerSerializer(data=data, context=context)
        if serializer.is_valid(raise_exception=True):
            response = serializer.create_stripe_customer(data)
            if response[1] == True:
                return Response(data=response[0], status=status.HTTP_200_OK)
            return Response({'error':response[0]}, status=response[2])

class NewPaypalCustomer(APIView):
    permission_classes = (permissions.AllowAny,)
    # authentication_classes = (SessionAuthentication,)
    def post(self, request):
        data = request.data
        validated_subscriber_id = validate_subscriber_id(data)
        if validated_subscriber_id[0] == False:
            return Response(data=validated_subscriber_id[1], status=validated_subscriber_id[2])

        context = {'user': request.user}
        serializer = NewPaypalCustomerSerializer(data=data, context=context)
        if serializer.is_valid(raise_exception=True):
            response = serializer.create_paypal_customer(data)
            if response[1] == True:
                return Response(data=response[0], status=status.HTTP_200_OK)
            return Response({'error':response[0]}, status=response[2])

class NewCoinbaseCustomer(APIView):
    permission_classes = (permissions.AllowAny,)
    # authentication_classes = (SessionAuthentication,)
    def post(self, request):
        data = request.data
        validated_charge_url = validate_charge_url(data)
        if validated_charge_url[0] == False:
            return Response(data=validated_charge_url[1], status=validated_charge_url[2])

        context = {'user': request.user}
        serializer = NewCoinbaseCustomerSerializer(data=data, context=context)
        if serializer.is_valid(raise_exception=True):
            response = serializer.create_coinbase_customer(data)
            if response[1] == True:
                return Response(data=response[0], status=status.HTTP_200_OK)
            return Response({'error':response[0]}, status=response[2])

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def processView(request):
    subscriber = does_subscriber_exist(request)
    subscribed = is_user_subscribed(request, subscriber)
    if subscribed == False:
        if request.data.get('method') == 'Paypal':
            subscriber_id = request.data.get('subscriptionID')
            save_subscriber(request, 'Paypal', subscriber, subscriber_id=subscriber_id)
            return Response(status=status.HTTP_200_OK)
        
    subscriber.stripe_url, subscriber.coinbase_url, subscriber.stripe_customer_id = None, None, None
    
    serializer = ProcessSerializer(subscriber)
    return Response(data=serializer.data,
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
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def successView(request):
    subscriber = does_subscriber_exist(request)
    method = obtain_method(subscriber)
    subscribed = is_user_subscribed(request, subscriber)
    if subscribed == True:
        return_url = request.data.get('return_url')
        subscriber.url = None
        subscriber.status = None
        
        if method == 'Stripe':
            stripe_portal = build_stripe_portal(request, subscriber, return_url)
            subscriber.url = stripe_portal.url
            return Response({'url':stripe_portal.url},
                            status=status.HTTP_200_OK)

        if method == 'Coinbase':
            client = Client(api_key=settings.COINBASE_COMMERCE_API_KEY)
            charge_id = decrypt(subscriber.subscription_id)
            charge = client.charge.retrieve(charge_id)
            subscriber.url = charge.hosted_url
        
        if method == 'Paypal':
            subscription_id = decrypt(subscriber.subscription_id)
            if request.data.get('action') == None:
                details = show_sub_details(subscription_id)
                subscriber.status = details['status']
            elif request.data.get('action') == 'Stop':
                suspend_sub(subscription_id)
                return Response(status=status.HTTP_200_OK)
            elif request.data.get('action') == 'Re-start':
                activate_sub(subscription_id)
                return Response(status=status.HTTP_200_OK)
        
        serializer = SuccessSerializer(subscriber)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    else:
        subscriber.url = None
        subscriber.status = None
        serializer = SuccessSerializer(subscriber)
        return Response(data=serializer.data,
                    status=status.HTTP_200_OK)