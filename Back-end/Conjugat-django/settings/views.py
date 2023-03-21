from .models import Theme, TwoFactorAuth
from .totp import create_key_of_length, generate_QR_string_and_code
from coinbase_commerce.client import Client

from django.conf import settings
from django.contrib.auth.models import User
from knox import views as Knox_views
from subscription.encryption import decrypt, encrypt
from subscription.models import UserProfile
from subscription.paypal import show_sub_details, suspend_sub, activate_sub, cancel_sub
import stripe
from verbs.models import Progress
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes


from rest_framework import status, permissions
from rest_framework.authentication import SessionAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ChangeEmailSerializer, ChangePasswordSerializer, \
    ChangeUsernameSerializer, ThemeSerializer, TwoFactorAuthSerializer, \
    CloseAccountSerializer
from .validations import *

''' Routes '''
class GetRoutes(APIView):
    def get(self, request):
        routes = [
        {
            'Endpoint': '/change-email/',
            'method': 'POST',
            'body': {'body': ""},
            'description': "Change the user's email"
        },
        {
            'Endpoint': '/change-password/',
            'method': 'POST',
            'body': {'body': ""},
            'description': "Change the user's password"
        },
        {
            'Endpoint': '/change-username/',
            'method': 'POST',
            'body': {'body': ""},
            'description': "Change the user's username"
        },
        {
            'Endpoint': '/reset-account/',
            'method': 'GET, POST',
            'body': {'body': ""},
            'description': "Reset a user's account"
        },
        {
            'Endpoint': '/close-account/',
            'method': 'POST',
            'body': {'body': ""},
            'description': "Close an account"
        },
        {
            'Endpoint': '/premium/',
            'method': 'GET, POST',
            'body': {'body': ""},
            'description': "Check the user's payment status"
        },
        {
            'Endpoint': '/themes/',
            'method': 'POST',
            'body': {'body': ""},
            'description': "Change the theme"
        },
        {
            'Endpoint': '/two-factor-auth/',
            'method': 'GET, POST',
            'body': {'body': ""},
            'description': "Add or remove 2FA"
        },
    ]
        return Response(routes)


''' Change email '''
class ChangeEmail(APIView):
    permission_classes = (permissions.AllowAny,)
    # authentication_classes = (SessionAuthentication,)
    def post(self, request):
        data = request.data
        assert validate_email(data)
        assert validate_password(data)
        context = {'username': request.user.username}
        serializer = ChangeEmailSerializer(data=data, context=context)
        if serializer.is_valid(raise_exception=True):
            response = serializer.change_email(data)
            if response[1] == True:
                return Response(data=response[0], status=status.HTTP_200_OK)
            return Response({'error':response[0]}, status=response[2])


''' Change password '''
class ChangePassword(APIView):
    permission_classes = (permissions.AllowAny,)
    # authentication_classes = (SessionAuthentication,)
    def post(self, request):
        data = request.data
        assert validate_password(data)
        assert validate_new_passwords(data)
        context = {'username': request.user.username}
        serializer = ChangePasswordSerializer(data=data, context=context)
        if serializer.is_valid(raise_exception=True):
            response = serializer.change_password(data)
            if response[1] == True:
                return Response(data=response[0], status=status.HTTP_200_OK)
            return Response({'error':response[0]}, status=response[2])
      

''' Change username '''
class ChangeUsername(APIView):
    permission_classes = (permissions.AllowAny,)
    # authentication_classes = (SessionAuthentication,)
    def post(self, request):
        data = request.data
        assert validate_username(data)
        assert validate_password(data)
        context = {'username': request.user.username}
        serializer = ChangeUsernameSerializer(data=data, context=context)
        if serializer.is_valid(raise_exception=True):
            response = serializer.change_username(data)
            if response[1] == True:
                return Response(data=response[0], status=status.HTTP_200_OK)
            return Response({'error':response[0]}, status=response[2])


''' Reset account '''
@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def resetAccountView(request):
    if request.method == "GET":
        account = Progress.objects.filter(user=request.user)
        try:
            languages = [account[x].language for x in account]
        except:
            languages = None
        return Response({'languages':languages})
        
    elif request.method == "POST":
        languages = request.data.get("languages")
        password = request.data.get("password")

        if not password:
            print('No password provided')
            return Response({'error': 'No password provided'},
                            status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.get(username=request.user)
        if user.check_password(password) == False:
            print('Incorrect password')
            return Response({'error': 'Incorrect password'},
                            status=status.HTTP_400_BAD_REQUEST)
        for language in languages:
            try:
                account = Progress.objects.get(user=request.user, language=language)
            except:
                account = None
            if account:
                    account.delete()

        return Response({"success": "Account was successfully reset"},
                status=status.HTTP_200_OK)


''' Close account '''
class CloseAccount(APIView):
    permission_classes = (permissions.AllowAny,)
    # authentication_classes = (SessionAuthentication,)
    def post(self, request):
        data = request.data
        assert validate_password(data)
        context = {'username': request.user.username}
        serializer = CloseAccountSerializer(data=data, context=context)
        if serializer.is_valid(raise_exception=True):
            response = serializer.close_account(data)
            if response[1] == True:
                return Response(data=response[0], status=status.HTTP_200_OK)
            return Response({'error':response[0]}, status=response[2])



from subscription.serializers import ProcessSerializer, SuccessSerializer

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

def is_user_subscribed(request, subscriber):
    if subscriber:
        subscribed = subscriber.subscribed
    else:
        subscriber = UserProfile.objects.create(user=request.user, method_id=payment_method('None'))
        subscriber.save()
    return subscribed

def payment_method(method):
    if method == 'Stripe':
        return 1
    elif method == 'Paypal':
        return 2
    elif method == 'Coinbase':
        return 3
    elif method == 'None':
        return 4

def obtain_method(subscriber):
    if subscriber:
        method = str(subscriber.method)
    else:
        method = None
    return method

def does_subscriber_exist(request):
    try:
        subscriber = UserProfile.objects.get(user=request.user)
    except:
        subscriber = UserProfile.objects.create(user=request.user, method_id=payment_method('None'))
        subscriber.save()
    return subscriber

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
        checkout_kwargs['local_price']['amount'] = '3.00'
    
    charge = client.charge.create(**checkout_kwargs)
    return charge

def build_stripe_portal(request, subscriber, return_url):
    customer = decrypt(subscriber.customer_id)
    portalSession = stripe.billing_portal.Session.create(
                    customer=customer,
                    return_url=return_url,
    )
    return portalSession

''' Premium view '''
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def premiumView(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    subscriber = does_subscriber_exist(request)
    method = obtain_method(subscriber)
    subscribed = is_user_subscribed(request, subscriber)
    print(subscribed)
    if subscribed == False:
        print(method)
        if request.data.get('method') == None:
            success_url = request.data.get("success_url")
            cancel_url = request.data.get("cancel_url")

            customer = stripe.Customer.create()
            stripe_url = build_stripe_checkout(request, subscriber, customer, success_url, cancel_url).url
            subscriber.stripe_customer_id = customer.id
            subscriber.stripe_url = stripe_url

            charge = build_coinbase_checkout(subscriber, success_url, cancel_url)
            coinbase_url = charge.hosted_url
            subscriber.coinbase_url = coinbase_url

            serializer = ProcessSerializer(subscriber)
            return Response(data=serializer.data,
                            status=status.HTTP_200_OK)
        
        if request.data.get('method') == 'Stripe':
            customer_id = request.data.get('customer_id')
            try:
                save_subscriber(request, 'Stripe', subscriber, customer_id = customer_id)
            except:
                return Response(status=status.HTTP_404_NOT_FOUND)
            return Response(status=status.HTTP_200_OK)

        if request.data.get('method') == 'Paypal':
            subscriber_id = request.data.get('subscriptionID')
            save_subscriber(request, 'Paypal', subscriber, subscriber_id=subscriber_id)
            return Response(status=status.HTTP_200_OK)
        
        if request.data.get('method') == 'Coinbase':
            charge_url = request.data.get('charge_url')
            subscriber_id = charge_url.rsplit('/', 1)[1]
            try:
                save_subscriber(request, 'Coinbase', subscriber, subscriber_id=subscriber_id)
            except:
                return Response(status=status.HTTP_404_NOT_FOUND)
            return Response(status=status.HTTP_200_OK)
    else:
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



''' Theme '''
class ChangeTheme(APIView):
    permission_classes = (permissions.AllowAny,)
    # authentication_classes = (SessionAuthentication,)
    def post(self, request):
        data = request.data
        assert validate_choice(data)
        context = {'username': request.user}
        serializer = ThemeSerializer(data=data, context=context)
        if serializer.is_valid(raise_exception=True):
            response = serializer.change_theme(data)
            if response[1] == True:
                return Response(data=response[0], status=status.HTTP_200_OK)
            return Response({'error':response[0]}, status=response[2])


''' 2FA '''
class TwoFactorAuthentication(APIView):
    permission_classes = (permissions.AllowAny,)
    # authentication_classes = (SessionAuthentication,)
    def doesTwoFactorExist(self, request):
        try:
            TwoFactor = TwoFactorAuth.objects.get(user=request.user)
            confirmed = TwoFactor.confirmed
        except:
            TwoFactor = None
            confirmed = None
        return TwoFactor, confirmed
    
    def get(self, request):
        TwoFactor, confirmed = self.doesTwoFactorExist(request)
        if not TwoFactor or TwoFactor.confirmed == False:
            key = create_key_of_length(20)
            if not TwoFactor:
                TwoFactor = TwoFactorAuth.objects.create(user=request.user)
            TwoFactor.key = encrypt(key.decode('ascii'))
            TwoFactor.save()
            email = User.objects.get(username=request.user).email
            qr_string = generate_QR_string_and_code(key, email)
            context = {'qr_string':qr_string, 'confirmed':confirmed}
            return Response(data=context)
        else:
            key = decrypt(TwoFactor.key).encode('ascii')
            email = User.objects.get(username=request.user).email
            qr_string = generate_QR_string_and_code(key, email)
            context = {'qr_string':qr_string, 'confirmed':confirmed}
            return Response(data=context)
        
    def post(self, request):
        data = request.data
        length_of_OTP = 6
        assert validate_password(data)
        assert validate_totp(data, length_of_OTP)
        context = {'username': request.user}
        serializer = TwoFactorAuthSerializer(data=data, context=context)
        if serializer.is_valid(raise_exception=True):
            response = serializer.set_2FA(data)
            if response[1] == True:
                return Response(data=response[0], status=status.HTTP_200_OK)
            return Response({'error':response[0]}, status=response[2])
        











