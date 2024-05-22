# serializers.py

from rest_framework import serializers
from .models import user_signup, user_Profile
from django.contrib.auth.hashers import make_password


class UserSignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = user_signup
        fields = ["fullname", "username", "email", "password"]

    def create(self, validated_data):
        validated_data["password"] = make_password(validated_data["password"])
        return super(UserSignupSerializer, self).create(validated_data)

    def update(self, instance, validated_data):
        if "password" in validated_data:
            validated_data["password"] = make_password(validated_data["password"])
        return super(UserSignupSerializer, self).update(instance, validated_data)


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=50)
    password = serializers.CharField(max_length=255, write_only=True)


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSignupSerializer(read_only=True)

    class Meta:
        model = user_Profile
        fields = [
            "id",
            "user",
            "first_name",
            "last_name",
            "mobile_number",
            "profile_image",
            "created_on",
            "updated_on",
        ]
