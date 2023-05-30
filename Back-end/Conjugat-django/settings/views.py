from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from .models import Theme, Font, FontDB, Typeface, Language, TwoFactorAuth
from rest_framework import status, permissions
from rest_framework.authentication import SessionAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ChangeEmailSerializer, ChangePasswordSerializer, \
    ChangeUsernameSerializer, ThemeSerializer, LanguageSerializer, FontSerializer, \
TwoFactorAuthSerializer, ResetAccountSerializer, CloseAccountSerializer, PremiumSerializer
from subscription.encryption import decrypt, encrypt
from .totp import create_key_of_length, generate_QR_string_and_code
from .validations import *
from verbs.models import RomanceTestResult_by_user_and_language, RomanceTestResult


''' Routes '''
class GetRoutes(APIView):
    def get(self, request):
        routes = [
        {
            'Endpoint': '/change-email/',
            'method': 'POST',
            'body': {'body': ""},
            'description': "Change the user's email"
        },
        {
            'Endpoint': '/change-password/',
            'method': 'POST',
            'body': {'body': ""},
            'description': "Change the user's password"
        },
        {
            'Endpoint': '/change-username/',
            'method': 'POST',
            'body': {'body': ""},
            'description': "Change the user's username"
        },
        {
            'Endpoint': '/reset-account/',
            'method': 'GET, POST',
            'body': {'body': ""},
            'description': "Reset a user's account"
        },
        {
            'Endpoint': '/close-account/',
            'method': 'POST',
            'body': {'body': ""},
            'description': "Close an account"
        },
        {
            'Endpoint': '/premium/',
            'method': 'GET, POST',
            'body': {'body': ""},
            'description': "Check the user's payment status"
        },
        {
            'Endpoint': '/themes/',
            'method': 'POST',
            'body': {'body': ""},
            'description': "Change the theme"
        },
        {
            'Endpoint': '/two-factor-auth/',
            'method': 'GET, POST',
            'body': {'body': ""},
            'description': "Add or remove 2FA"
        },
    ]
        return Response(routes)


''' Change email '''
# @method_decorator(csrf_protect, name='dispatch')
class ChangeEmail(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request):
        data = request.data
        validated_email = validate_email(data)
        validated_password = validate_password(data)
        if validated_email[0] == False:
            return Response(data=validated_email[1], status=validated_email[2])
        if validated_password[0] == False:
            return Response(data=validated_password[1], status=validated_password[2])

        context = {'username': request.user.username}
        serializer = ChangeEmailSerializer(data=data, context=context)
        if serializer.is_valid(raise_exception=True):
            response = serializer.change_email(data)
            if response[1] == True:
                return Response(data=response[0], status=status.HTTP_200_OK)
            return Response({'error':response[0]}, status=response[2])


''' Change password '''
class ChangePassword(APIView):
    permission_classes = (permissions.AllowAny,)
    # authentication_classes = (SessionAuthentication,)
    def post(self, request):
        data = request.data
        validated_password = validate_password(data)
        validated_new_passwords = validate_new_passwords(data)
        if validated_password[0] == False:
            return Response(data=validated_password[1], status=validated_password[2])
        if validated_new_passwords[0] == False:
            return Response(data=validated_new_passwords[1], status=validated_new_passwords[2])

        context = {'username': request.user.username}
        serializer = ChangePasswordSerializer(data=data, context=context)
        if serializer.is_valid(raise_exception=True):
            response = serializer.change_password(data)
            if response[1] == True:
                return Response(data=response[0], status=status.HTTP_200_OK)
            return Response({'error':response[0]}, status=response[2])
      

''' Change username '''
class ChangeUsername(APIView):
    permission_classes = (permissions.AllowAny,)
    # authentication_classes = (SessionAuthentication,)
    def post(self, request):
        data = request.data
        validated_password = validate_password(data)
        validated_new_passwords = validate_new_passwords(data)
        if validated_password[0] == False:
            return Response(data=validated_password[1], status=validated_password[2])
        if validated_new_passwords[0] == False:
            return Response(data=validated_new_passwords[1], status=validated_new_passwords[2])
        assert validate_username(data)
        assert validate_password(data)
        context = {'username': request.user.username}
        serializer = ChangeUsernameSerializer(data=data, context=context)
        if serializer.is_valid(raise_exception=True):
            response = serializer.change_username(data)
            if response[1] == True:
                return Response(data=response[0], status=status.HTTP_200_OK)
            return Response({'error':response[0]}, status=response[2])


''' Font '''
class ReadFonts(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    def get(self, request):
        try:
            fonts = FontDB.objects.all()
        except:
            fonts = None
        
        data = {"fonts": {"font": [], "typeface": []}, "typefaces": []}
        if fonts:
            for font in fonts:
                data["fonts"]["font"].append(font.font)
                data["fonts"]["typeface"].append(font.typeface)
        typefaces = Typeface.objects.all()
        if typefaces:
            for typeface in typefaces:
                data["typefaces"].append(typeface.typeface)
        return Response(data=data, status=status.HTTP_200_OK)

class ChangeFont(APIView):
    permission_classes = (permissions.AllowAny,)
    def get(self, request):
        try:
            headerFont = Font.objects.get(user=request.user).headerFont
            bodyFont = Font.objects.get(user=request.user).bodyFont
        except:
            headerFont = Font.objects.create(user=request.user).headerFont
            bodyFont = Font.objects.create(user=request.user).bodyFont

        data = {
            "headerFont": headerFont.font,
            "bodyFont": bodyFont.font
        }
        return Response(data=data, status=status.HTTP_200_OK)
    
    def post(self, request):
        data = request.data
        validate_header_font = validate_header_font(data)
        validate_body_font = validate_body_font(data)
        if validate_header_font[0] == False:
            return Response(data=validate_header_font[1], status=validate_header_font[2])
        if validate_body_font[0] == False:
            return Response(data=validate_body_font[1], status=validate_body_font[2])

        context = {'username': request.user}
        serializer = FontSerializer(data=data, context=context)
        if serializer.is_valid(raise_exception=True):
            response = serializer.change_font(data)
            if response[1] == True:
                return Response(data=response[0], status=status.HTTP_200_OK)
            return Response({'error':response[0]}, status=response[2])


''' Language '''
class ReadLanguages(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    def get(self, request):
        try:
            languages = Language.objects.all()
        except:
            languages = None
        
        data = {"language": []}
        if languages:
            for language in languages:
                data["language"].append(language.language)
        return Response(data=data, status=status.HTTP_200_OK)

class ChangeLanguage(APIView):
    permission_classes = (permissions.AllowAny,)
    def get(self, request):
        try:
            language = Language.objects.get(user=request.user).language
        except:
            language = Language.objects.create(user=request.user).language
        return Response({'language':language}, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        validated_choice = validate_choice(data)
        if validated_choice[0] == False:
            return Response(data=validated_choice[1], status=validated_choice[2])

        context = {'username': request.user}
        serializer = LanguageSerializer(data=data, context=context)
        if serializer.is_valid(raise_exception=True):
            response = serializer.change_language(data)
            if response[1] == True:
                return Response(data=response[0], status=status.HTTP_200_OK)
            return Response({'error':response[0]}, status=response[2])


''' Logout all '''
class Logout_all(APIView):
    def post(self, request):
        request.user.auth_token_set.all().delete()
        logout(request)
        success = "User has been successfully logged out"
        return Response({"success": success},
                    status=status.HTTP_204_NO_CONTENT)

from django.core.cache import cache
''' Reset account '''
class ResetAccount(APIView):
    permission_classes = (permissions.AllowAny,)
    # authentication_classes = (SessionAuthentication,)
    def get(self, request):
        languages = []
        options = ['English', 'French', 'Italian', 'Portuguese', 'Spanish']
        for option in options:
            try:
                # Move this to cache?
                language = RomanceTestResult_by_user_and_language.objects.filter(pk=option, user=request.user.id).first()
            except:
                language = None
            if language:
                languages.append(option)
        return Response({'languages':languages})

    def post(self, request):
        data = request.data
        validated_password = validate_password(data)
        if validated_password[0] == False:
            return Response(data=validated_password[1], status=validated_password[2])
    
        context = {'user': request.user}
        serializer = ResetAccountSerializer(data=data, context=context)
        if serializer.is_valid(raise_exception=True):
            response = serializer.reset_account(data)
            if response[1] == True:
                return Response(data=response[0], status=status.HTTP_200_OK)
            return Response({'error':response[0]}, status=response[2])


''' Close account '''
class CloseAccount(APIView):
    permission_classes = (permissions.AllowAny,)
    # authentication_classes = (SessionAuthentication,)
    def post(self, request):
        data = request.data
        validated_password = validate_password(data)
        if validated_password[0] == False:
            return Response(data=validated_password[1], status=validated_password[2])

        context = {'user': request.user}
        serializer = CloseAccountSerializer(data=data, context=context)
        if serializer.is_valid(raise_exception=True):
            response = serializer.close_account(data)
            if response[1] == True:
                return Response(data=response[0], status=status.HTTP_200_OK)
            return Response({'error':response[0]}, status=response[2])




''' Premium view '''
class Premium(APIView):
    permission_classes = (permissions.AllowAny,)
    # authentication_classes = (SessionAuthentication,)
    def post(self, request):
        data = request.data
        context = {'user': request.user}
        serializer = PremiumSerializer(data=data, context=context)
        if serializer.is_valid(raise_exception=True):
            response = serializer.return_premium_status(data)
            if response[1] == True:
                return Response(data=response[0], status=status.HTTP_200_OK)
            return Response({'error':response[0]}, status=response[2])


''' Theme '''
# @method_decorator(csrf_protect, name='dispatch')
class ChangeTheme(APIView):
    permission_classes = (permissions.AllowAny,)
    def get(self, request):
        try:
            theme = Theme.objects.get(user=request.user).theme
        except:
            theme = Theme.objects.create(user=request.user).theme
        return Response({'theme':theme}, status=status.HTTP_200_OK)
    
    def post(self, request):
        data = request.data
        validated_choice = validate_choice(data)
        if validated_choice[0] == False:
            return Response(data=validated_choice[1], status=validated_choice[2])

        context = {'username': request.user}
        serializer = ThemeSerializer(data=data, context=context)
        if serializer.is_valid(raise_exception=True):
            response = serializer.change_theme(data)
            if response[1] == True:
                return Response(data=response[0], status=status.HTTP_200_OK)
            return Response({'error':response[0]}, status=response[2])


''' Language '''
# @method_decorator(csrf_protect, name='dispatch')
class ChangeLanguage(APIView):
    permission_classes = (permissions.AllowAny,)
    def get(self, request):
        try:
            language = Language.objects.get(user=request.user).language
        except:
            language = Language.objects.create(user=request.user).language
        return Response({'language':language}, status=status.HTTP_200_OK)
    
    def post(self, request):
        data = request.data
        validated_choice = validate_choice(data)
        if validated_choice[0] == False:
            return Response(data=validated_choice[1], status=validated_choice[2])

        context = {'username': request.user}
        serializer = LanguageSerializer(data=data, context=context)
        if serializer.is_valid(raise_exception=True):
            response = serializer.change_language(data)
            if response[1] == True:
                return Response(data=response[0], status=status.HTTP_200_OK)
            return Response({'error':response[0]}, status=response[2])


''' 2FA '''
class TwoFactorAuthentication(APIView):
    permission_classes = (permissions.AllowAny,)
    # authentication_classes = (SessionAuthentication,)
    def doesTwoFactorExist(self, request):
        try:
            TwoFactor = TwoFactorAuth.objects.get(user=request.user)
            confirmed = TwoFactor.confirmed
        except:
            TwoFactor = None
            confirmed = None
        return TwoFactor, confirmed
    
    def get(self, request):
        TwoFactor, confirmed = self.doesTwoFactorExist(request)
        if not TwoFactor or TwoFactor.confirmed == False:
            key = create_key_of_length(20)
            if not TwoFactor:
                TwoFactor = TwoFactorAuth.objects.create(user=request.user)
            TwoFactor.key = encrypt(key.decode('ascii'))
            TwoFactor.save()
            email = User.objects.get(username=request.user).email
            qr_string = generate_QR_string_and_code(key, email)
            context = {'qr_string':qr_string, 'confirmed':confirmed}
            return Response(data=context)
        else:
            key = decrypt(TwoFactor.key).encode('ascii')
            email = User.objects.get(username=request.user).email
            qr_string = generate_QR_string_and_code(key, email)
            context = {'qr_string':qr_string, 'confirmed':confirmed}
            return Response(data=context)
        
    def post(self, request):
        data = request.data
        length_of_OTP = 6
        validated_password = validate_password(data)
        if validated_password[0] == False:
            return Response(data=validated_password[1], status=validated_password[2])
        validated_totp = validate_totp(data, length_of_OTP)
        if validated_totp[0] == False:
            return Response(data=validated_totp[1], status=validated_totp[2])

        context = {'username': request.user}
        serializer = TwoFactorAuthSerializer(data=data, context=context)
        if serializer.is_valid(raise_exception=True):
            response = serializer.set_2FA(data)
            if response[1] == True:
                return Response(data=response[0], status=status.HTTP_200_OK)
            return Response({'error':response[0]}, status=response[2])