from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
import json

# I don't want to do anything with the mailchimp webhooks as I can just use mailchimp instead of storing data on my site as well.
@csrf_exempt
def mailchimp_webhooks(request):
    try:
        payload = request.body
        event = json.loads(payload)
    except ValueError as e:
        print("Webhook error while parsing basic request." + str(e))
        return JsonResponse({"success": False}, status=400)
    return JsonResponse({"success": True}, status=200)
