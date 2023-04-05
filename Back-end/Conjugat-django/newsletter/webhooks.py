from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import NewsletterSubscriber

def get_subscriber(email):
    user = User.objects.get(email=email)
    subscriber = NewsletterSubscriber(user=user)
    return subscriber

def subscription_method(status):
    if status == 'subscribe':
        return 1
    if status == 'unsubscribe':
        return 2
    if status == 'non-subscribed':
        return 3
    if status == 'cleaned':
        return 4
    if status == 'pending':
        return 5

@csrf_exempt
def mailchimp_webhooks(request):
    try:
        payload = request.body
        event = json.loads(payload)
    except ValueError as e:
        print("Webhook error while parsing basic request." + str(e))
        return JsonResponse({"success": False}, status=400)
    
    try:
        print(event["type"]) # log event
        subscriber = get_subscriber(event['data']['email'])
        subscriber.status = subscription_method(event["type"])
        subscriber.save()
        return JsonResponse({"success": True}, status=200)
    except:
        return JsonResponse({"success":False}, status=400)