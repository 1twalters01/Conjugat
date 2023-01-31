from .encryption import decrypt, encrypt
from .models import UserProfile
from coinbase_commerce.error import SignatureVerificationError, WebhookInvalidPayload
from coinbase_commerce.webhook import Webhook
from dateutil.relativedelta import relativedelta
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from datetime import date
import json


def payment_method(method):
    if method == 'Stripe':
        return 1
    elif method == 'Paypal':
        return 2
    elif method == 'Coinbase':
        return 3

def get_subscriber_or_none(subscription_id, method):
    try:
        # Retrieve UserProfile instance with the subscription id
        subscribers = UserProfile.objects.filter(method_id=payment_method(method))
        x = None
        for i in range(len(subscribers)):
            if decrypt(subscribers[i].subscription_id) == (subscription_id):
                x = i
                break
        subscriber = subscribers[x]
    except:
        subscriber = None
    return subscriber


def get_customer_or_none(customer_id, method):
    try:
        # Retrieve UserProfile instance with said subscription id
        customers = UserProfile.objects.filter(method_id=payment_method(method), subscribed=True)
        x = None
        for i in range(len(customers)):
            if decrypt(customers[i].customer_id) == (customer_id):
                x = i
                break
        customer = customers[x]
    except:
        # No subscription with that id saved in our database
        customer = None
    return customer


@csrf_exempt
def stripe_webhooks(request):
    try:
        payload = request.body
        event = json.loads(payload)
    except ValueError as e:
        print("Webhook error while parsing basic request." + str(e))
        return JsonResponse({"success": True}, status=400)


    if event and event["type"] == "customer.deleted":
        print("customer.deleted") # log event
        customer_id = event["data"]["object"]["id"]
        req_userprofile = get_customer_or_none(customer_id, 'Stripe')
        print(req_userprofile)
        if req_userprofile:
            # Remove the subscription id from the database and set to false
            user = req_userprofile.user
            subscriber = UserProfile.objects.get(user=user)
            subscriber.subscribed = False
            subscriber.save()
            return JsonResponse({"success": True}, status=200)
        return JsonResponse({"success": False}, status=500)


    elif event and event["type"] == "invoice.payment_succeeded":
        print("invoice.payment_succeeded") # log event
        customer_id = event["data"]["object"]["customer"]
        subscription_id = event["data"]["object"]["id"]
        req_userprofile = get_customer_or_none(customer_id, 'Stripe')
        if req_userprofile:
            # Add the subscription id to the database

            user = req_userprofile.user
            subscriber = UserProfile.objects.get(user=user)
            subscriber.subscription_id = encrypt(subscription_id)
            subscriber.customer_id = encrypt(customer_id)
            subscriber.subscribed = True
            subscriber.start_date = date.today()
            if subscriber.trial == False:
                subscriber.end_date = date.today() + relativedelta(months=1) + relativedelta(days=2)
            else:
                subscriber.end_date = date.today() + relativedelta(days = 7)
            subscriber.trial = False
            subscriber.save()
            return JsonResponse({"success": True}, status=200)
        return JsonResponse({"success": False}, status=500)


    elif event and event["type"] == "customer.subscription.trial_will_end":
        print("customer.subscription.trial_will_end") # log event
        customer_id = event["data"]["object"]["customer"]
        req_userprofile = get_customer_or_none(customer_id, 'Stripe')
        if req_userprofile:
            user = User.objects.get(username=req_userprofile.user)
            email = user.email
            subject = f"Your Conjugat free trial"
            message = f"Your Conjugat free trial is ending. Please sign in at conjugat.io to find out more"
            send_mail(subject, message, settings.EMAIL_HOST_USER, email)
            return JsonResponse({"success": True}, status=200)
        return JsonResponse({"success": False}, status=500)











@csrf_exempt
def paypal_webhooks(request):
    try:
        payload = request.body
        event = json.loads(payload)
    except ValueError as e:
        print("Webhook error while parsing basic request." + str(e))
        return JsonResponse({"success": True}, status=400)

    # If the subscription gets activated
    if event and event["event_type"] == "BILLING.SUBSCRIPTION.ACTIVATED":
        print("Billing.subscription.activated") # log event
        subscription_id = event['resource']['id']
        req_userprofile = get_subscriber_or_none(subscription_id, 'Paypal')
        if req_userprofile:
            # Add the subscription id to the database
            user = req_userprofile.user
            subscriber = UserProfile.objects.get(user=user)
            subscriber.subscription_id = encrypt(subscription_id)
            subscriber.subscribed = True
            subscriber.start_date = date.today()
            if subscriber.trial == False:
                subscriber.end_date = date.today() + relativedelta(months=1) + relativedelta(days=2)
            else:
                subscriber.end_date = date.today() + relativedelta(days = 7)
            subscriber.trial = False
            subscriber.save()
            return JsonResponse({"success": True}, status=200)
        return JsonResponse({"success": False}, status=500)
    

    # Whenever I get paid
    elif event and event["event_type"] == "PAYMENT.SALE.COMPLETED":
        print("PAYMENT.SALE.COMPLETED") # log event
        subscription_id = event['resource']['id']
        req_userprofile = get_subscriber_or_none(subscription_id, 'Paypal')
        if req_userprofile:
            user = req_userprofile.user
            subscriber = UserProfile.objects.get(user=user)
            subscriber.subscription_id = encrypt(subscription_id)
            subscriber.subscribed = True
            subscriber.start_date = date.today()
            if subscriber.trial == False:
                subscriber.end_date = date.today() + relativedelta(months=1) + relativedelta(days=2)
            else:
                subscriber.end_date = date.today() + relativedelta(days = 7)
            subscriber.trial = False
            subscriber.save()
            return JsonResponse({"success": True}, status=200)
        return JsonResponse({"success": False}, status=500)


    # If it becomes expired
    elif event and event["event_type"] == "Billing.subscription.expired":
        print("Billing.subscription.expired") # log event
        subscription_id = event['resource']['id']
        req_userprofile = get_subscriber_or_none(subscription_id, 'Paypal')
        if req_userprofile:
            user = req_userprofile.user
            subscriber = UserProfile.objects.get(user=user)
            subscriber.subscribed = False
            subscriber.trial = False
            subscriber.save()
            return JsonResponse({"success": True}, status=200)
        return JsonResponse({"success": False}, status=500)











@csrf_exempt
@require_http_methods(['POST'])
def coinbase_webhooks(request):
    request_data = request.body.decode('utf-8')
    request_sig = request.headers.get('X-CC-Webhook-Signature', None)
    webhook_secret = settings.COINBASE_COMMERCE_WEBHOOK_SECRET

    try:
        event = Webhook.construct_event(request_data, request_sig, webhook_secret)
    except (SignatureVerificationError, WebhookInvalidPayload) as e:
        print("Webhook error while parsing basic request." + str(e))
        return JsonResponse({"success": True}, status=400)
    
    if event['type'] == 'charge:created':
        subscription_id = event['data']['code']
        req_userprofile = get_subscriber_or_none(subscription_id, 'Coinbase')
        if req_userprofile:
            return JsonResponse({"success": True}, status=200)

    elif event['type'] == 'charge:confirmed':
        print('charge:confirmed') # log event
        subscription_id = event['data']['code']
        req_userprofile = get_subscriber_or_none(subscription_id, 'Coinbase')
        if req_userprofile:
            # Add the subscription id to the database
            user = req_userprofile.user
            subscriber = UserProfile.objects.get(user=user)
            subscriber.subscription_id = encrypt(subscription_id)
            subscriber.subscribed = True
            subscriber.start_date = date.today()
            if subscriber.trial == False:
                subscriber.end_date = date.today() + relativedelta(months=1) + relativedelta(days=2)
            else:
                subscriber.end_date = date.today() + relativedelta(days = 7)
            subscriber.trial = False
            subscriber.save()
            return JsonResponse({"success": True}, status=200)
        return JsonResponse({"success": False}, status=500)