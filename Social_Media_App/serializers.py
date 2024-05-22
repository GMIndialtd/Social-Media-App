# serializers.py

from rest_framework import serializers
from .models import user_signup


class UserSignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = user_signup
        fields = ["fullname", "username", "email", "password"]


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=50)
    password = serializers.CharField(max_length=255)
