from rest_framework import serializers
from .models import user_signup, UserProfile
from django.contrib.auth.hashers import make_password


class UserSignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = user_signup
        fields = ["username", "email", "password"]

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


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = "__all__"
