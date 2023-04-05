from django.conf import settings
from django.contrib.auth.models import User
import hashlib
from mailchimp_marketing import Client
from mailchimp_marketing.api_client import ApiClientError
from .models import NewsletterSubscriber
from rest_framework import serializers, status


''' Subscribe '''
class SubscribeSerializer(serializers.Serializer):
    email = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField(required=False)
    def create_member(self, email, languages, first_name, last_name):
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

    def subscribe_user(self, data):
        email = data['email']
        first_name = data['first_name']
        last_name = data['last_name']
        languages = data['languages']
        
        mailchimp = Client()
        mailchimp.set_config({
            'api_key': settings.MAILCHIMP_API_KEY,
            'server': settings.MAILCHIMP_REGION,
        })

        try:
            member_info = self.create_member(email, languages, first_name, last_name)
            mailchimp.lists.add_list_member(
                settings.MAILCHIMP_MARKETING_AUDIENCE_ID,
                member_info,
            )
        except:
            try:
                email_hash = hashlib.md5(email.encode('utf-8').lower()).hexdigest()
                member_update = {'status': 'subscribed',}
                mailchimp.lists.update_list_member(
                    settings.MAILCHIMP_MARKETING_AUDIENCE_ID,
                    email_hash,
                    member_update,
                )
            except ApiClientError as error:
                return error.text, False, status.HTTP_424_FAILED_DEPENDENCY
        
        response = 'Successfully subscribed to the newsletter'
        return response, True


''' Unsubscribe '''
class UnsubscribeSerializer(serializers.Serializer):
    email = serializers.CharField()
    def unsubscribe_user(self, data):
        email = data['email']

        mailchimp = Client()
        mailchimp.set_config({
            'api_key': settings.MAILCHIMP_API_KEY,
            'server': settings.MAILCHIMP_REGION,
        })


        try:
            email_hash = hashlib.md5(email.encode('utf-8').lower()).hexdigest()
            member_update = {'status': 'unsubscribed',}
            response = mailchimp.lists.update_list_member(
                settings.MAILCHIMP_MARKETING_AUDIENCE_ID,
                email_hash,
                member_update,
            )

        except ApiClientError as error:
            return error.text, False, status.HTTP_424_FAILED_DEPENDENCY
        
        response = 'Successfully unsubscribed from the newsletter'
        return response, True
    
''' Obtain status '''
class StatusSerializer(serializers.Serializer):
    status = serializers.CharField()
    def get_subscriber(self, user):
        try:
            subscriber = NewsletterSubscriber.objects.get(user=user)
        except:
            subscriber = None
        return subscriber
    
    def NewsletterStatus(self, status):
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
    
    def get_status(self, data):
        username =  self.context['username']
        user = User.objects.get(username=username)
        subscriber = self.get_subscriber(user)
        if not subscriber:
            subscriber = NewsletterSubscriber.objects.create(user=user)
            subscriber.status = self.NewsletterStatus('Not-subscribed')

        if not subscriber.status:
            subscriber.status = self.NewsletterStatus('Not-subscribed')
        elif subscriber.status:
            response = {'status': subscriber.status}
        return response, True