from .forms import InfoForm, EmailForm
from django.conf import settings
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
import hashlib
from mailchimp_marketing import Client
from mailchimp_marketing.api_client import ApiClientError


from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.authtoken.models import Token


@api_view(["GET"])
@permission_classes([AllowAny])
def getRoutes(request):
    routes = [
        {
            'Endpoint': '/subscribe/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Subscribes to the newsletter'
        },
        {
            'Endpoint': '/unsubscribe/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Unsubscribes to the newsletter'
        },
    ]
    return Response(routes)


''' Mailchimp ping '''
mailchimp = Client()
mailchimp.set_config({
  'api_key': settings.MAILCHIMP_API_KEY,
  'server': settings.MAILCHIMP_REGION,
})

#Check if mailchimp is working
def mailchimp_ping_view(request):
    response = mailchimp.ping.get()
    return JsonResponse(response)


''' Subscribe'''
def does_email_exist(request):
    email = None
    if request.user.is_authenticated:
        try:
            email = User.objects.get(username=request.user).email
        except:
            email = None
    return email


def create_member(email, languages, first_name, last_name):
    member_info = {
            'email_address': email,
            'status': 'subscribed',
            'merge_fields': {
                'FNAME': first_name,
            }
        }
    if last_name:
        member_info['merge_fields']['last_name'] = last_name
    if languages:
        member_info['tags'] = languages
    return member_info


@api_view(["GET", "POST"])
@permission_classes([AllowAny])
def subscribeView(request):
    if request.method == 'GET':
        email = does_email_exist(request)
        return Response({'email':email},
                        status=status.HTTP_200_OK)

    if request.method == 'POST':
        email = request.data.get('email')
        first_name = request.data.get('')
        last_name = request.data.get('')
        languages = request.data.get('languages')

        if not email:
            error = 'No email provided'
            print(error)
            return Response({'error':error},
                        status=status.HTTP_400_BAD_REQUEST)

        if not first_name:
            error = 'No first name provided'
            print(error)
            return Response({'error':error},
                        status=status.HTTP_400_BAD_REQUEST)

        if not last_name:
            last_name = None
        if not languages:
            languages = None

        try:
            member_info = create_member(email, languages, first_name, last_name)
            mailchimp.lists.add_list_member(
                settings.MAILCHIMP_MARKETING_AUDIENCE_ID,
                member_info,
            )

        except ApiClientError as error:
            return HttpResponse(error.text)
        
        success = 'Successfully subscribed to the newsletter'
        return Response({'success':success, 'unsubscribe':True},
                        status=status.HTTP_200_OK)








''' Unsubscribe '''
@api_view(["POST"])
@permission_classes([AllowAny])
def unsubscribeView(request):
    email = request.data.get('email')
    if not email:
        error = 'No email provided'
        print(error)
        return Response({'error':error},
                    status=status.HTTP_400_BAD_REQUEST)

    try:
        email_hash = hashlib.md5(email.encode('utf-8').lower()).hexdigest()
        member_update = {'status': 'unsubscribed',}
        response = mailchimp.lists.update_list_member(
            settings.MAILCHIMP_MARKETING_AUDIENCE_ID,
            email_hash,
            member_update,
        )

    except ApiClientError as error:
        return HttpResponse(error.text)
    
    success = 'Successfully unsubscribed from the newsletter'
    return Response({'success':success, 'unsubscribe':True},
                    status=status.HTTP_200_OK)