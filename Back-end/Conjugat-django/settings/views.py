from .forms import CloseAccountForm, ChangePasswordForm, ChangeEmailForm, ChangeUsernameForm, ThemesForm, TOTPForm, ResetAccountForm
from .models import Theme, TwoFactorAuth
from .totp import create_key_of_length, generate_totp, generate_QR_string_and_code
from coinbase_commerce.client import Client
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView#
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from subscription.encryption import decrypt, encrypt
from subscription.models import UserProfile
from subscription.paypal import show_sub_details, suspend_sub, activate_sub, cancel_sub
import stripe
from verbs.models import Progress

from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes

@api_view(["GET"])
@permission_classes([AllowAny])
def getRoutes(request):
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


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def changeEmailView(request):
    email = request.data.get("email")
    password = request.data.get("password")

    if not email:
        print('No password provided')
        return Response({'error': 'No email provided'},
                        status=status.HTTP_400_BAD_REQUEST)
    if not password:
        print('No password provided')
        return Response({'error': 'No password provided'},
                        status=status.HTTP_400_BAD_REQUEST)
    
    user = User.objects.get(username=request.user)
    
    if user.check_password(password) == False:
        print('Incorrect password')
        return Response({'error': 'Incorrect password'},
                        status=status.HTTP_400_BAD_REQUEST)
    
    try:
        check = User.objects.get(email=email)
    except:
        check = None

    if check:
        print('Email is already in use')
        return Response({'error': 'Email is already in use'},
                        status=status.HTTP_400_BAD_REQUEST)
    if check == None:
        user.email = email
        user.save()
    return Response({"success": "Email changed successfully"},
                status=status.HTTP_200_OK)

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def changePasswordView(request):
    password = request.data.get("password")
    newPassword1 = request.data.get("newPassword1")
    newPassword2 = request.data.get("newPassword2")

    if not password:
        print('No password provided')
        return Response({'error': 'No password provided'},
                        status=status.HTTP_400_BAD_REQUEST)
    if not newPassword1:
        print('No new password provided')
        return Response({'error': 'No new password provided'},
                        status=status.HTTP_400_BAD_REQUEST)
    if not newPassword2:
        print('No verification password provided')
        return Response({'error': 'No verification password provided'},
                        status=status.HTTP_400_BAD_REQUEST)
    
    user = User.objects.get(username=request.user)
    if user.check_password(password) == False:
        print('Incorrect password')
        return Response({'error': 'Incorrect password'},
                        status=status.HTTP_400_BAD_REQUEST)
    
    if newPassword1 != newPassword2:
        print('Passwords do not match')
        return Response({'error': 'Passwords do not match'},
                        status=status.HTTP_400_BAD_REQUEST)

    user.set_password(newPassword1)
    user.save()
    return Response({"success": "Password was changed successfully"},
                status=status.HTTP_200_OK)

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def changeUsernameView(request):
    username = request.data.get("username")
    password = request.data.get("password")

    if not username:
        print('No username provided')
        return Response({'error': 'No username provided'},
                        status=status.HTTP_400_BAD_REQUEST)
    if not password:
        print('No password provided')
        return Response({'error': 'No password provided'},
                        status=status.HTTP_400_BAD_REQUEST)
    
    user = User.objects.get(username=request.user)
    
    if user.check_password(password) == False:
        print('Incorrect password')
        return Response({'error': 'Incorrect password'},
                        status=status.HTTP_400_BAD_REQUEST)
    
    try:
        check = User.objects.get(username=username)
    except:
        check = None

    if check:
        print('Username is already in use')
        return Response({'error': 'Username is already in use'},
                        status=status.HTTP_400_BAD_REQUEST)
    if check == None:
        user.username = username
        user.save()
    return Response({"success": "Username changed successfully"},
                status=status.HTTP_200_OK)


def payment_method(method):
    if method == 'Stripe':
        return 1
    elif method == 'Paypal':
        return 2
    elif method == 'Coinbase':
        return 3

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def closeAccountView(request):
    password = request.data.get('password')
    
    if not password:
        print('No password provided')
        return Response({'error': 'No password provided'},
                        status=status.HTTP_400_BAD_REQUEST)

    user = User.objects.get(username=request.user)
    if user.check_password(password) == False:
        print('Incorrect password')
        return Response({'error': 'Incorrect password'},
                        status=status.HTTP_400_BAD_REQUEST)
    
    try:
        premium = UserProfile.objects.get(user=request.user)
    except:
        premium = None

    if premium:
        if premium.subscribed == True:
            if premium.method_id == payment_method('Stripe'):
                # stop subscription
                if premium.subscription_id:
                    try:
                        subscription = decrypt(premium.subscription_id)
                        stripe.api_key = settings.STRIPE_SECRET_KEY
                        stripe.Subscription.delete(subscription)
                    except:
                        error = 'Invalid stripe subscription id'
                        print(error)
                        return Response({'error': error},
                            status=status.HTTP_400_BAD_REQUEST)
            if premium.method_id == payment_method('Paypal'):
                try:
                    cancel_sub(decrypt(premium.subscription_id))
                except:
                    error = 'invalid paypal subscription id'
                    print(error)
                    return Response({'error': error},
                                    status=status.HTTP_400_BAD_REQUEST)
        premium.delete()

    user.delete()
    success = 'Account deleted successfully'
    return Response({'success':success},
        status=status.HTTP_200_OK)



@api_view(["POST"])
@permission_classes([IsAuthenticated])
def themesView(request):
    choice = request.data.get("choice")
    if not choice:
        print('No theme provided')
        return Response({'error': 'No theme provided'},
                        status=status.HTTP_400_BAD_REQUEST)
                        
    theme = Theme.objects.get_or_create(user=request.user)[0]

    if choice != 'Light':
        if choice != 'Dark':
            print('Invalid option')
            return Response({'error': 'Invalid option'},
                            status=status.HTTP_400_BAD_REQUEST)
    theme.theme = choice
    theme.save()
    return Response({"success": "Theme changed successfully"},
                status=status.HTTP_200_OK)




@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def premiumView(request):
    if request.method == 'GET':
        try:
            user = UserProfile.objects.get(user=request.user)
            subscribed = user.subscribed
            method = user.method_method
        except:
            user = None
            subscribed = None
            method = None

        context = {'method':method, 'subscribed':subscribed}

        if method == None:
            pass
        elif method == 'Stripe':
            pass
        elif method == 'Paypal':
            sub_id = decrypt(user.subscription_id)
            paypalStatus = show_sub_details(sub_id)['status']
            context['status'] = paypalStatus
        elif method == 'Coinbase':
            charge_id = decrypt(user.subscription_id)
            client = Client(api_key=settings.COINBASE_COMMERCE_API_KEY)
            charge = client.charge.retrieve(charge_id)
            context['charge'] = charge
        else:
            error = 'invalid payment method'
            print(error)
            return Response({'error':error},
                status=status.HTTP_400_BAD_REQUEST)
        # Add serializers
        return Response({'context':context},
                        status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'POST':
        subscribed = request.data.get('premium')
        method = request.data.get('method')

        if not subscribed:
            error = 'No subscription status provided'
            print(error)
            return Response({'error':error},
                status=status.HTTP_400_BAD_REQUEST)
        if not method:
            error = 'No payment method provided'
            print(error)
            return Response({'error':error},
                status=status.HTTP_400_BAD_REQUEST)

        try:
            user = UserProfile.objects.get(user=request.user)
        except:
            user = None
        if not user:
            error = 'user is not valid'
            print(error)
            return Response({'error':error}, 
                status=status.HTTP_400_BAD_REQUEST)
        if user.method_method != method:
            error ='posted method does not match stored payment method'
            print(error)
            return Response({'error':error},
                status=status.HTTP_400_BAD_REQUEST)
        if user.subscribed != subscribed:
            error ='posted subscription status does not match stored status'
            print(error)
            return Response({'error':error},
                status=status.HTTP_400_BAD_REQUEST)
        
        if user.method_id == payment_method('Stripe'):
            try:
                return_url = request.data.get['return_url']
                portalSession = stripe.billing_portal.Session.create(
                    customer = decrypt(user.customer_id),
                    return_url=return_url,
                )
            except:
                error = 'Invalid customer ID'
                print(error)
                return Response({'error':error},
                                status=status.HTTP_400_BAD_REQUEST)
            return Response({'url':portalSession.url},
                status=status.HTTP_303_SEE_OTHER)

        elif user.method_id == payment_method('Paypal'):
            sub_id = decrypt(user.subscription_id)
            if request.data.get('Stop'):
                try:
                    suspend_sub(sub_id)
                except:
                    error = 'Invalid subscription ID'
                    print(error)
                    return Response({'error':error},
                                    status=status.HTTP_400_BAD_REQUEST)
                success = 'successfully paused subscription'
                return Response({'success':success},
                    status=status.HTTP_200_OK)

            elif request.data.get('Re-start'):
                try:
                    activate_sub(sub_id)
                except:
                    error = 'Invalid subscription ID'
                    print(error)
                    return Response({'error':error},
                                    status=status.HTTP_400_BAD_REQUEST)
                
                success = 'successfully re-started subscription'
                return Response({'success':success},
                    status=status.HTTP_200_OK)
            
            else:
                error = 'invalid paypal method'
                print(error)
                return Response({'error':error},
                    status=status.HTTP_400_BAD_REQUEST)

        elif user.method_id == payment_method('Coinbase'):
            error ='Coinbase option has no post request'
            print(error)
            return Response({'error':error},
                status=status.HTTP_400_BAD_REQUEST)
        
        else:
            error = 'invalid payment method'
            print(error)
            return Response({'error':error},
                status=status.HTTP_400_BAD_REQUEST)




def doesTwoFactorExist(request):
    try:
        TwoFactor = TwoFactorAuth.objects.get(user=request.user)
        confirmed = TwoFactor.confirmed
    except:
        TwoFactor = None
        confirmed = None
    return TwoFactor, confirmed

@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def twoFactorAuthView(request):
    TwoFactor, confirmed = doesTwoFactorExist(request)
    length_of_OTP = 6
    step_in_seconds = 30

    if request.method == "GET":
        if not TwoFactor or TwoFactor.confirmed == False:
            key = create_key_of_length(20)
            if not TwoFactor:
                TwoFactor = TwoFactorAuth.objects.create(user=request.user)
            TwoFactor.key = encrypt(key.decode('ascii'))
            TwoFactor.save()
            email = User.objects.get(username=request.user).email
            qr_string = generate_QR_string_and_code(key, email, length_of_OTP, step_in_seconds)
            # Use serializer
            print(qr_string)
            context = {'qr_string':qr_string, 'confirmed':confirmed}
            return Response(data=context)

        else:
            key = decrypt(TwoFactor.key).encode('ascii')

            email = User.objects.get(username=request.user).email
            qr_string = generate_QR_string_and_code(key, email, length_of_OTP, step_in_seconds)
            # Use serializer
            context = {'qr_string':qr_string, 'confirmed':confirmed}
            return Response(data=context)

    elif request.method == "POST":
        password = request.data.get("password")
        totp = request.data.get("totp")
        if not password:
            print('No password provided')
            return Response({'error': 'No password provided'},
                            status=status.HTTP_400_BAD_REQUEST)
        if not totp:
            print('No totp provided')
            return Response({'error': 'No totp provided'},
                            status=status.HTTP_400_BAD_REQUEST)

        if totp.isnumeric() == False:
            print('totp must only contain numbers')
            return Response({'error': 'totp must only contain numbers'},
                            status=status.HTTP_400_BAD_REQUEST)
        
        if len(totp) != length_of_OTP:
            error = 'totp must be ' + str(length_of_OTP) + ' characters long'
            print(error)
            return Response({'error': error},
                            status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.get(username=request.user)
        if user.check_password(password) == False:
            print('Incorrect password')
            return Response({'error': 'Incorrect password'},
                            status=status.HTTP_400_BAD_REQUEST)

        key = decrypt(TwoFactor.key).encode('ascii')
        totpGenerated = generate_totp(key, length_of_OTP, step_in_seconds)
        
        if int(totp) != int(totpGenerated):
            error = 'Incorrect totp'
            print(error)
            return Response({'error':error},
                status=status.HTTP_400_BAD_REQUEST)

        if TwoFactor.confirmed == False:
            TwoFactor.confirmed = True
            TwoFactor.save()
            success = "Two factor authentication has been added"
            return Response({"success": success},
                status=status.HTTP_200_OK)

        elif TwoFactor.confirmed == True:
            TwoFactor.confirmed = False
            TwoFactor.save()
            success = "Two factor authentication has been removed"
            return Response({"success": success},
                status=status.HTTP_200_OK)

        else:
            print('Error in Two factor confirmation')
            return Response({'error': 'Error in Two factor confirmation'},
                            status=status.HTTP_400_BAD_REQUEST)




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

