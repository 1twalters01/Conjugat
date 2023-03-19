from django.conf import settings
import hashlib
from mailchimp_marketing import Client
from mailchimp_marketing.api_client import ApiClientError
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