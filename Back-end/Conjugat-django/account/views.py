from django.contrib.auth import logout
from rest_framework import status, permissions
from rest_framework.authentication import SessionAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import LoginUsernameSerializer, LoginPasswordSerializer, \
RegisterSerializer, ActivateSerializer, PasswordResetSerializer, PasswordResetConfirmSerializer
from .validations import *


''' Routes '''
class GetRoutes(APIView):
    def get(self, request):
        routes = [
        {
            'Endpoint': '/login/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Check if the user has totp activated'
        },
        {
            'Endpoint': '/login/password/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Authenticates the user'
        },
        {
            'Endpoint': '/logout/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Logs out the user'
        },
        {
            'Endpoint': '/register/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Registers a new, unactivated user'
        },
        {
            'Endpoint': '/activate/<uidb64>/<token>/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Activate a newly registered user'
        },
        {
            'Endpoint': '/password-reset/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Send a password reset email'
        },
        {
            'Endpoint': '/password-reset/<uidb64>/<token>/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Reset a password for a user'
        },
    ]
        return Response(routes)


''' Login '''
class LoginUsername(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = (SessionAuthentication,)
    def post(self, request):
        data = request.data
        assert validate_username(data)
        serializer = LoginUsernameSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            response = serializer.check_username(data)
            if response[1] == True:
                return Response(data=response[0], status=status.HTTP_200_OK)
            return Response({'error':response[0]}, status=status.HTTP_404_NOT_FOUND)

class LoginPassword(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = (SessionAuthentication,)
    def post(self, request):
        data = request.data
        assert validate_username(data)
        assert validate_password(data)
        serializer = LoginPasswordSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            response = serializer.login_user(data)
            if response[1] == True:
                return Response(data=response[0], status=status.HTTP_200_OK)
            return Response({'error':response[0]}, status=response[2])


''' Logout '''
class Logout(APIView):
    def post(self, request):
        request.user.auth_token.delete()
        logout(request)
        success = "User has been successfully logged out"
        return Response({"success": success},
                    status=status.HTTP_204_NO_CONTENT)


''' Register '''
# I am using django to send the email. I could use mailchimp instead.
class Register(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = (SessionAuthentication,)
    def post(self, request):
        data = request.data
        assert validate_username(data)
        assert validate_email(data)
        assert validate_passwords(data)
        assert validate_domain(data)
        serializer = RegisterSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            response = serializer.register_user(data)
            if response[1] == True:
                return Response(data=response[0], status=status.HTTP_201_CREATED)
            return Response({'error':response[0]}, status=response[2])

class Activate(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = ()
    def post(self, request):
        data = request.data
        assert validate_uidb64(data)
        assert validate_token(data)
        serializer = ActivateSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            response = serializer.activate_user(data)
            if response[1] == True:
                return Response({"success":response[0]}, status=status.HTTP_200_OK)
            return Response({'error':response[0]}, status=status.HTTP_400_BAD_REQUEST)


''' Password reset '''
class PasswordReset(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = (SessionAuthentication,)
    def post(self, request):
        data = request.data
        assert validate_email(data)
        assert validate_domain(data)
        serializer = PasswordResetSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            response = serializer.send_password_reset_email(data)
            if response[1] == True:
                return Response(data=response[0], status=status.HTTP_200_OK)
            return Response({'error':response[0]}, status=response[2])

class PasswordResetConfirm(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = ()
    def post(self, request):
        data = request.data
        assert validate_uidb64(data)
        assert validate_token(data)
        assert validate_passwords(data)
        serializer = PasswordResetConfirmSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            response = serializer.activate_user(data)
            if response[1] == True:
                return Response({"success":response[0]}, status=status.HTTP_200_OK)
            return Response({'error':response[0]}, status=status.HTTP_400_BAD_REQUEST)