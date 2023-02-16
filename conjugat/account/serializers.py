from rest_framework import serializers

from django.contrib.auth.models import User

class ReadOnlyModelSerializer(serializers.ModelSerializer):
    def get_fields(self, *args, **kwargs):
        fields = super().get_fields(*args, **kwargs)
        for field in fields:
            fields[field].read_only = True
        return fields

class LoginUsernameSerializer(ReadOnlyModelSerializer):
    confirmed = serializers.BooleanField(allow_null=True)
    class Meta:
        model = User
        fields = ('username', 'id', 'confirmed')