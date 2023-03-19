from django.contrib.auth.models import User
from rest_framework import status, permissions
from rest_framework.authentication import SessionAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import SubscribeSerializer, UnsubscribeSerializer
from .validations import *


''' Routes '''
class GetRoutes(APIView):
    def get(self, request):
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


''' Subscribe'''
class Subscribe(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = (SessionAuthentication,)
    def get(self, request):
        email = ''
        if request.user.is_authenticated:
            try:
                email = User.objects.get(username=request.user).email
            except:
                email = ''
        return Response({'email':email},
                        status=status.HTTP_200_OK)
    def post(self, request):
        data = request.data
        assert validate_email(data)
        assert validate_first_name(data)
        serializer = SubscribeSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            response = serializer.subscribe_user(data)
            if response[1] == True:
                return Response(data=response[0], status=status.HTTP_201_CREATED)
            return Response({'error':response[0]}, status=response[2])


''' Unsubscribe '''
class Unsubscribe(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = (SessionAuthentication,)
    def get(self, request):
        email = ''
        if request.user.is_authenticated:
            try:
                email = User.objects.get(username=request.user).email
            except:
                email = ''
        return Response({'email':email},
                        status=status.HTTP_200_OK)
    def post(self, request):
        data = request.data
        assert validate_email(data)
        serializer = UnsubscribeSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            response = serializer.unsubscribe_user(data)
            if response[1] == True:
                return Response(data=response[0], status=status.HTTP_201_CREATED)
            return Response({'error':response[0]}, status=response[2])