from coinbase_commerce.client import Client
import datetime
from django.conf import settings
from django.contrib.auth.models import User
from django.core.cache import cache
from subscription.encryption import decrypt, encrypt
from rest_framework import serializers, status
from settings.models import Theme, Language, Font, TwoFactorAuth
from settings.totp import generate_totp
from subscription.encryption import decrypt
from subscription.models import UserProfile
from subscription.paypal import show_sub_details, suspend_sub, activate_sub, cancel_sub
import stripe
from verbs.models import RomanceTestResult_by_user_and_language, RomanceTestResult_by_user_and_date, RomanceTestResult


class ChangeEmailSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()
    def validate_email(self, email):
        try:
            validated_email = User.objects.get(email=email)
        except:
            validated_email = None
        if validated_email:
            error = 'Email is already in use'
            return error, False, status.HTTP_400_BAD_REQUEST
        return True, True
    
    def change_email(self, data):
        email = data['email']
        password = data['password']
        username =  self.context['username']

        user = User.objects.get(username=username)
        if user.check_password(password) == False:
            error = "Incorrect password"
            return error, False, status.HTTP_400_BAD_REQUEST
        
        validated_email = self.validate_email(email)
        if validated_email[1] == False:
            return validated_email[0], validated_email[1], validated_email[2]
        
        user.email = email
        user.save()
        response = "Email changed successfully"
        return response, True

class ChangePasswordSerializer(serializers.Serializer):
    password = serializers.CharField()
    newPassword1 = serializers.CharField()
    newPassword2 = serializers.CharField()
    def change_password(self, data):
        password = data['password']
        newPassword1 = data['newPassword1']
        newPassword2 = data['newPassword2']
        username =  self.context['username']

        user = User.objects.get(username=username)
        if user.check_password(password) == False:
            error = "Incorrect password"
            return error, False, status.HTTP_400_BAD_REQUEST
        
        if newPassword1 != newPassword2:
            error = "Passwords do not match"
            return error, False, status.HTTP_400_BAD_REQUEST

        user.set_password(newPassword1)
        user.save()
        response = "Password changed successfully"
        return response, True

class ChangeUsernameSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    def validate_username(self, username):
        try:
            validated_username = User.objects.get(username=username)
        except:
            validated_username = None
        if validated_username:
            error = 'Username is already in use'
            return error, False, status.HTTP_400_BAD_REQUEST
        return True, True
    
    def change_username(self, data):
        username = data['username']
        password = data['password']
        req_username =  self.context['username']

        user = User.objects.get(username=req_username)
        if user.check_password(password) == False:
            error = "Incorrect password"
            return error, False, status.HTTP_400_BAD_REQUEST
        
        validated_email = self.validate_username(username)
        if validated_email[1] == False:
            return validated_email[0], validated_email[1], validated_email[2]
        
        user.username = username
        user.save()
        response = "Email changed successfully"
        return response, True

class ResetAccountSerializer(serializers.Serializer):
    password = serializers.CharField()
    def reset_account(self, data):
        languages = data["languages"]
        password = data["password"]

        req_user = self.context['user']
        user = User.objects.get(username=req_user.username)
        if user.check_password(password) == False:
            error = 'Incorrect password'
            return error, False, status.HTTP_400_BAD_REQUEST

        for language in languages:
            try:
                testIDs = RomanceTestResult_by_user_and_language.objects.filter(pk=language, user=req_user.id)
                for testID in testIDs:
                    try:
                        testCache = cache.get(key=testID.testID)
                    except:
                        testCache = []
                    print(testCache)
                    values = []
                    for index, choice in enumerate(testCache['languages']):
                        if choice == language:
                            values.append(index)

                    testCache['pks'] = [v for i, v in enumerate(testCache['pks']) if i not in values]
                    testCache['ranks'] = [v for i, v in enumerate(testCache['ranks']) if i not in values]
                    testCache['languages'] = [v for i, v in enumerate(testCache['languages']) if i not in values]
                    testCache['bases'] = [v for i, v in enumerate(testCache['bases']) if i not in values]
                    testCache['tenses'] = [v for i, v in enumerate(testCache['tenses']) if i not in values]
                    testCache['subjects'] = [v for i, v in enumerate(testCache['subjects']) if i not in values]
                    testCache['auxiliaries'] = [v for i, v in enumerate(testCache['auxiliaries']) if i not in values]
                    testCache['conjugations'] = [v for i, v in enumerate(testCache['conjugations']) if i not in values]
                    testCache['answers'] = [v for i, v in enumerate(testCache['answers']) if i not in values]
                    testCache['status'] = [v for i, v in enumerate(testCache['status']) if i not in values]
                    print('l')
                    if not testCache['pks'] and not testCache['ranks'] and not testCache['languages'] and not testCache['bases'] and not testCache['tenses'] and not testCache['subjects'] and not testCache['auxiliaries'] and not testCache['conjugations'] and not testCache['answers'] and not testCache['status']:

                        # Delete the cache's testID result
                        cache.delete(key=testID.testID)

                        # Delete the cache from the cache's user lists
                        cacheList = cache.get(key=req_user.username)
                        try:
                            cacheList.remove(testID.testID)
                            cache.set(key=req_user.username, value=cacheList)
                        except:
                            None

                        # Delete the user and date
                        try:
                            datedResult = RomanceTestResult_by_user_and_date.objects.get(pk=req_user.id, testID=testID.testID)
                        except:
                            datedResult = None
                        if datedResult:
                            datedResult.delete()
                        
                        # Delete the main cassandra entry
                        try:
                            mainResult = RomanceTestResult.objects.get(pk=testID.testID)
                        except:
                            mainResult = None
                        if mainResult:
                            mainResult.delete()

                        # Delete the user and language
                        try:
                            languageResult = RomanceTestResult_by_user_and_language.objects.get(pk=language, testID=testID.testID)
                        except:
                            languageResult = None
                        if languageResult:
                            languageResult.delete()
            except:
                None

        response = 'Account was successfully reset'
        return response, True

class CloseAccountSerializer(serializers.Serializer):
    password = serializers.CharField()
    def totp_validation(self, user, totp):
        try:
            TwoFactor = TwoFactorAuth.objects.get(user=user.id)
            key = decrypt(TwoFactor.key).encode('ascii')
            totpCheck = generate_totp(key)
        except:
            TwoFactor = None
            totpCheck = ''

        if totpCheck != totp:
            error = 'The totp is incorrect'
            return error, False, status.HTTP_400_BAD_REQUEST
        return True, True

    def delete_premium(self, req_username):
        try:
            premium = UserProfile.objects.get(user=req_username)
        except:
            premium = None

        if premium:
            if premium.subscribed == True:
                if premium.method_id == self.payment_method('Stripe'):
                    # stop subscription
                    if premium.subscription_id:
                        try:
                            subscription = decrypt(premium.subscription_id)
                            stripe.api_key = settings.STRIPE_SECRET_KEY
                            stripe.Subscription.delete(subscription)
                        except:
                            error = 'Invalid stripe subscription id'
                            return error, False, status.HTTP_400_BAD_REQUEST
                            
                if premium.method_id == self.payment_method('Paypal'):
                    try:
                        cancel_sub(decrypt(premium.subscription_id))
                    except:
                        error = 'invalid paypal subscription id'
                        return error, False, status.HTTP_400_BAD_REQUEST
            premium.delete()
            return True, True

    def payment_method(self, method):
        if method == 'Stripe':
            return 1
        elif method == 'Paypal':
            return 2
        elif method == 'Coinbase':
            return 3
        elif method == 'None':
            return 4

    def close_account(self, data):
        password = data['password']
        totp = data['totp']
        req_user = self.context['user']
        user = User.objects.get(username=req_user.username)

        if user.check_password(password) == False:
            error = 'Incorrect password'
            return error, False, status.HTTP_400_BAD_REQUEST

        validated_totp = self.totp_validation(user, totp)
        if validated_totp[1] == False:
            return validated_totp[0], validated_totp[1], validated_totp[2]

        delete_premium_check = self.delete_premium(req_user.username)
        if delete_premium_check[1] == False:
            return delete_premium_check[0], delete_premium_check[1], delete_premium_check[2]

        # Delete Cassandra
        try:
            testIDs = RomanceTestResult_by_user_and_language.objects.filter(pk__in=['English', 'French', 'Italian', 'Portuguese', 'Spanish'], user=req_user.id.id)
        except:
            testIDs = None
        if testIDs:
            for testID in testIDs:
                test = RomanceTestResult.objects.filter(pk=testID.testID)
                test.delete()
            testIDs.delete()
        try:
            testIDs = RomanceTestResult_by_user_and_date.objects.filter(pk=req_user.id, EndDateTime__gte=(datetime(year=2021, month=1, day=1)))
        except:
            testIDs = None
        if testIDs:
            testIDs.delete()
        
        # Delete redis
        cachedResults = cache.get(key=req_user.username)
        if cachedResults:
            for cachedResult in cachedResults:
                cache.delete(key=cachedResult)
            cache.delete(key=req_user.username)

        user.delete()
        response = 'Account deleted successfully'
        return response, True

class PremiumSerializer(serializers.Serializer):
    def does_subscriber_exist(self, user):
        try:
            subscriber = UserProfile.objects.get(user=user)
        except:
            subscriber = UserProfile.objects.create(user=user, method_id=self.payment_method('None'))
            subscriber.save()
        return subscriber
    
    def obtain_method(self, subscriber):
        if subscriber:
            method = str(subscriber.method)
        else:
            method = None
        return method
    
    def is_user_subscribed(self, user, subscriber):
        if subscriber:
            subscribed = subscriber.subscribed
        else:
            subscriber = UserProfile.objects.create(user=user, method_id=self.payment_method('None'))
            subscriber.save()
        return subscribed

    def build_stripe_checkout(self, subscriber, customer, success_url, cancel_url):
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

    def build_coinbase_checkout(self, subscriber, success_url, cancel_url):
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

    def payment_method(self, method):
        if method == 'Stripe':
            return 1
        elif method == 'Paypal':
            return 2
        elif method == 'Coinbase':
            return 3
        elif method == 'None':
            return 4

    def save_subscriber(self, user, subscriber, customer_id):
        if not subscriber:
            subscriber = UserProfile.objects.create(user=user, method_id=self.payment_method('Stripe'))
        subscriber.method_id=self.payment_method('Stripe')
        # Reset the subscription and customer ids
        subscriber.subscription_id = None
        subscriber.customer_id = encrypt(customer_id)
        subscriber.save()
    
    def build_stripe_portal(self, stripe, subscriber, return_url):
        customer = decrypt(subscriber.customer_id)
        portalSession = stripe.billing_portal.Session.create(
                        customer=customer,
                        return_url=return_url,
        )
        return portalSession

    def return_premium_status(self, data):
        user = self.context['user']
        stripe.api_key = settings.STRIPE_SECRET_KEY
        subscriber = self.does_subscriber_exist(user)
        method = self.obtain_method(subscriber)
        subscribed = self.is_user_subscribed(user, subscriber)
        if subscribed == False:
            if data['method'] == None:
                success_url = data["success_url"]
                cancel_url = data["cancel_url"]
                customer = stripe.Customer.create()
                stripe_url = self.build_stripe_checkout(subscriber, customer, success_url, cancel_url).url

                charge = self.build_coinbase_checkout(subscriber, success_url, cancel_url)
                coinbase_url = charge.hosted_url

                response = {
                    'subscribed':subscribed,
                    'trial':subscriber.trial,
                    'stripe_customer_id':customer.id,
                    'stripe_url':stripe_url,
                    'coinbase_url':coinbase_url
                }
                return response, True, status.HTTP_200_OK
            
            if data['method'] == 'Stripe':
                user = self.context['user']
                subscriber = self.does_subscriber_exist(user)
                subscribed = self.is_user_subscribed(user, subscriber)
                if subscribed == False:
                    customer_id = data['customer_id']
                    try:
                        self.save_subscriber(user, subscriber, customer_id)
                    except:
                        error = 'Stripe customer id was not found'
                        return error, False, status.HTTP_404_NOT_FOUND
                    response = "User created successfully"
                    return response, True, status.HTTP_200_OK

            if data['method'] == 'Paypal':
                user = self.context['user']
                subscriber = self.does_subscriber_exist(user)
                subscribed = self.is_user_subscribed(user, subscriber)
                if subscribed == False:
                    subscriber_id = data.get('subscriber_id')
                    try:
                        self.save_subscriber('Paypal', user, subscriber, subscriber_id)
                    except:
                        error = 'Paypal customer id was not found'
                        return error, False, status.HTTP_404_NOT_FOUND
                    response = "User created successfully"
                    return response, True, status.HTTP_200_OK
            
            if data['method'] == 'Coinbase':
                user = self.context['user']
                subscriber = self.does_subscriber_exist(user)
                subscribed = self.is_user_subscribed(user, subscriber)
                if subscribed == False:
                    charge_url = data['charge_url']
                    subscriber_id = charge_url.rsplit('/', 1)[1]
                    try:
                        self.save_subscriber('Coinbase', user, subscriber, subscriber_id)
                    except:
                        error = 'Coinbase id was not found'
                        return error, False, status.HTTP_404_NOT_FOUND
                    response = "User created successfully"
                    return response, True, status.HTTP_200_OK

        else:
            user = self.context['user']
            stripe.api_key = settings.STRIPE_SECRET_KEY
            subscriber = self.does_subscriber_exist(user)
            method = self.obtain_method(subscriber)
            subscribed = self.is_user_subscribed(user, subscriber)
            if subscribed == True:
                subscriber.url = None
                subscriber.status = None
                
                if method == 'Stripe':
                    return_url = data['return_url']
                    stripe_portal = self.build_stripe_portal(stripe, subscriber, return_url)
                    response = {
                        'method': method,
                        'subscribed': subscribed,
                        'url': stripe_portal.url
                    }
                    return response, True, status.HTTP_200_OK

                if method == 'Coinbase':
                    return_url = data['return_url']
                    client = Client(api_key=settings.COINBASE_COMMERCE_API_KEY)
                    charge_id = decrypt(subscriber.subscription_id)
                    charge = client.charge.retrieve(charge_id)
                    response = {
                        'method': method,
                        'subscribed': subscribed,
                        'url': charge.hosted_url
                    }
                    return response, True, status.HTTP_200_OK
                
                if method == 'Paypal':
                    action = data['action']
                    subscription_id = decrypt(subscriber.subscription_id)
                    if action == None:
                        details = show_sub_details(subscription_id)
                        subscriber.status = details['status']
                        response = {
                            'method': method,
                            'subscribed': subscribed,
                            'status': subscriber.status
                        }
                        return response, True, status.HTTP_200_OK
                    elif action == 'Stop':
                        suspend_sub(subscription_id)
                        details = show_sub_details(subscription_id)
                        subscriber.status = details['status']
                        response = {
                            'method': method,
                            'subscribed': subscribed,
                            'status': subscriber.status
                        }
                        return response, True, status.HTTP_200_OK
                    elif action == 'Re-start':
                        activate_sub(subscription_id)
                        details = show_sub_details(subscription_id)
                        subscriber.status = details['status']
                        response = {
                            'method': method,
                            'subscribed': subscribed,
                            'status': subscriber.status
                        }
                        return response, True, status.HTTP_200_OK


class ThemeSerializer(serializers.Serializer):
    choice = serializers.CharField()
    def validate_choice(self, choice):
        options = ['Dark', 'Light']
        if choice not in options:
            error = 'Invalid option'
            return error, False, status.HTTP_400_BAD_REQUEST
        return True, True
            
    def change_theme(self, data):
        choice = data['choice']
        req_username =  self.context['username']

        theme = Theme.objects.get_or_create(user=req_username)[0]

        validated_choice = self.validate_choice(choice)
        if validated_choice[1] == False:
            return validated_choice[0], validated_choice[1], validated_choice[2]
        
        theme.theme = choice
        theme.save()
        response = {"success":"Theme changed successfully", "theme":choice}
        return response, True


class LanguageSerializer(serializers.Serializer):
    choice = serializers.CharField()
    def validate_choice(self, choice):
        options = ["English", "French", "Italian", "Portuguese", "Spanish"]
        if choice not in options:
            error = 'Invalid option'
            return error, False, status.HTTP_400_BAD_REQUEST
        return True, True
            
    def change_language(self, data):
        choice = data['choice']
        req_username =  self.context['username']

        language = Language.objects.get_or_create(user=req_username)[0]

        validated_choice = self.validate_choice(choice)
        if validated_choice[1] == False:
            return validated_choice[0], validated_choice[1], validated_choice[2]
        
        language.language = choice
        language.save()
        response = {"success":"Language changed successfully", "language":choice}
        return response, True


class FontSerializer(serializers.Serializer):
    choice = serializers.CharField()
    def validate_choice(self, choice):
        options = ["open-dyslexic", "open-sans", "times-new-roman", "georgia", "lato"]
        if choice not in options:
            error = 'Invalid option'
            return error, False, status.HTTP_400_BAD_REQUEST
        return True, True
            
    def change_font(self, data):
        choice = data['choice']
        req_username =  self.context['username']

        font = Font.objects.get_or_create(user=req_username)[0]

        validated_choice = self.validate_choice(choice)
        if validated_choice[1] == False:
            return validated_choice[0], validated_choice[1], validated_choice[2]
        
        font.font = choice
        font.save()
        response = {"success": "Font changed successfully", "font":choice}
        return response, True

class TwoFactorAuthSerializer(serializers.Serializer):
    password = serializers.CharField()
    totp = serializers.CharField()
    def doesTwoFactorExist(self, req_username):
        try:
            TwoFactor = TwoFactorAuth.objects.get(user=req_username)
        except:
            TwoFactor = TwoFactorAuth.objects.create(user=req_username, confirmed=False)
        return TwoFactor
    
    def totp_validation(self, TwoFactor, totp):
        key = decrypt(TwoFactor.key).encode('ascii')
        totpGenerated = generate_totp(key)
        if int(totp) != int(totpGenerated):
            error = 'Incorrect totp'
            return error, False, status.HTTP_400_BAD_REQUEST
        return True, True
    
    def save_2FA(self, TwoFactor):
        if TwoFactor.confirmed == False:
            TwoFactor.confirmed = True
            TwoFactor.save()
            success = "Two factor authentication has been added"
            response = {"success": success, 'confirmed':TwoFactor.confirmed}
            return response, True, status.HTTP_200_OK

        elif TwoFactor.confirmed == True:
            TwoFactor.confirmed = False
            TwoFactor.save()
            success = "Two factor authentication has been removed"
            response = {"success": success, 'confirmed':TwoFactor.confirmed}
            return response, True, status.HTTP_200_OK

        else:
            error = 'Error in Two factor confirmation'
            return error, False, status.HTTP_400_BAD_REQUEST

    def set_2FA(self, data):
        password = data['password']
        totp = data['totp']
        req_username =  self.context['username']
        TwoFactor = self.doesTwoFactorExist(req_username)
        
        user = User.objects.get(username=req_username)
        if user.check_password(password) == False:
            error = 'Incorrect password'
            return error, False, status.HTTP_400_BAD_REQUEST

        
        validated_totp = self.totp_validation(TwoFactor, totp)
        if validated_totp[1] == False:
            return validated_totp[0], validated_totp[1], validated_totp[2]

        save_2FA = self.save_2FA(TwoFactor)
        return save_2FA[0], save_2FA[1], save_2FA[2]