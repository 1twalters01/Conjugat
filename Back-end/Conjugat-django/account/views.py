from django.contrib.auth import logout, login
from knox import views as Knox_views
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


# #For if I were to want to use session authentication
# ''' CSRF Token '''
# @method_decorator(ensure_csrf_cookie, name='dispatch')
# class GetCSRF(APIView):
#     def get(self, request):
#         token = get_token(request)
#         response = {'token': token}
#         return Response(data=response, status = status.HTTP_200_OK)


''' Login '''
class LoginUsername(APIView):
    permission_classes = (permissions.AllowAny,)
    # authentication_classes = (SessionAuthentication,)
    def post(self, request):
        data = request.data
        validated_username = validate_username(data)
        if validated_username[0] == False:
            return Response(data=validated_username[1], status=validated_username[2])
        
        serializer = LoginUsernameSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            response = serializer.check_username(data)
            if response[1] == True:
                return Response(data=response[0], status=status.HTTP_200_OK)
            return Response({'error':response[0]}, status=status.HTTP_404_NOT_FOUND)

class LoginPassword(Knox_views.LoginView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = (SessionAuthentication,)
    def post(self, request):
        data = request.data
        validated_username = validate_username(data)
        validated_password = validate_password(data)
        if validated_username[0] == False:
            return Response(data=validated_username[1], status=validated_username[2])
        if validated_password[0] == False:
            return Response(data=validated_password[1], status=validated_password[2])

        serializer = LoginPasswordSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            response = serializer.login_user(data)
            if response[1] == True:
                login(request, user=response[2], backend='django.contrib.auth.backends.ModelBackend')
                return Response(data=response[0], status=status.HTTP_200_OK)
            return Response({'error':response[0]}, status=status.HTTP_404_NOT_FOUND)


''' Logout '''
class Logout(APIView):
    def post(self, request):
        request._auth.delete()
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
        validated_username = validate_username(data)
        validated_passwords = validate_passwords(data)
        validated_domain = validate_domain(data)
        if validated_username[0] == False:
            return Response(data=validated_username[1], status=validated_username[2])
        if validated_passwords[0] == False:
            return Response(data=validated_passwords[1], status=validated_passwords[2])
        if validated_domain[0] == False:
            return Response(data=validated_domain[1], status=validated_domain[2])

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
        validated_uidb64 = validate_uidb64(data)
        validated_token = validate_uidb64(data)
        if validated_uidb64[0] == False:
            return Response(data=validated_uidb64[1], status=validated_uidb64[2])
        if validated_token[0] == False:
            return Response(data=validated_token[1], status=validated_token[2])

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
        validated_email = validate_email(data)
        validated_domain = validate_domain(data)
        if validated_email[0] == False:
            return Response(data=validated_email[1], status=validated_email[2])
        if validated_domain[0] == False:
            return Response(data=validated_domain[1], status=validated_domain[2])

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
        validated_uidb64 = validate_uidb64(data)
        validated_token = validate_token(data)
        validated_passwords = validate_passwords(data)
        if validated_uidb64[0] == False:
            return Response(data=validated_uidb64[1], status=validated_uidb64[2])
        if validated_token[0] == False:
            return Response(data=validated_token[1], status=validated_token[2])
        if validated_passwords[0] == False:
            return Response(data=validated_passwords[1], status=validated_passwords[2])

        serializer = PasswordResetConfirmSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            response = serializer.activate_user(data)
            if response[1] == True:
                return Response({"success":response[0]}, status=status.HTTP_200_OK)
            return Response({'error':response[0]}, status=status.HTTP_400_BAD_REQUEST)