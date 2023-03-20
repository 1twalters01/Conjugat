from django.contrib.auth.models import User
from rest_framework import serializers, status

class ChangeEmailSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()
    def validate_email(self, email):
        try:
            validated_email = User.objects.get(email=email)
        except:
            validated_email = None
        if validated_email:
            error = 'Email is already in use'
            return error, False, status.HTTP_400_BAD_REQUEST
        return True, True
    
    def change_email(self, data):
        email = data['email']
        password = data['password']
        username =  self.context['username']

        user = User.objects.get(username=username)
        if user.check_password(password) == False:
            error = "Incorrect password"
            return error, False, status.HTTP_400_BAD_REQUEST
        
        validated_email = self.validate_email(email)
        if validated_email[1] == False:
            return validated_email[0], validated_email[1], validated_email[2]
        
        user.email = email
        user.save()
        response = "Email changed successfully"
        return response, True

class ChangePasswordSerializer(serializers.Serializer):
    password = serializers.CharField()
    newPassword1 = serializers.CharField()
    newPassword2 = serializers.CharField()
    def change_password(self, data):
        password = data['password']
        newPassword1 = data['newPassword1']
        newPassword2 = data['newPassword2']
        username =  self.context['username']

        user = User.objects.get(username=username)
        if user.check_password(password) == False:
            error = "Incorrect password"
            return error, False, status.HTTP_400_BAD_REQUEST
        
        if newPassword1 != newPassword2:
            error = "Passwords do not match"
            return error, False, status.HTTP_400_BAD_REQUEST

        user.set_password(newPassword1)
        user.save()
        response = "Password changed successfully"
        return response, True

class ChangeUsernameSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    def validate_username(self, username):
        try:
            validated_username = User.objects.get(username=username)
        except:
            validated_username = None
        if validated_username:
            error = 'Username is already in use'
            return error, False, status.HTTP_400_BAD_REQUEST
        return True, True
    
    def change_username(self, data):
        username = data['username']
        password = data['password']
        req_username =  self.context['username']

        user = User.objects.get(username=req_username)
        if user.check_password(password) == False:
            error = "Incorrect password"
            return error, False, status.HTTP_400_BAD_REQUEST
        
        validated_email = self.validate_username(username)
        if validated_email[1] == False:
            return validated_email[0], validated_email[1], validated_email[2]
        
        user.username = username
        user.save()
        response = "Email changed successfully"
        return response, True