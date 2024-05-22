from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import user_signup, user_Profile
from .serializers import UserSignupSerializer, UserLoginSerializer, ProfileSerializer
from django.contrib.auth import authenticate
from rest_framework import generics
from rest_framework import status


@api_view(["POST"])
def signup(request):
    if request.method == "POST":
        serializer = UserSignupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "User created successfully"}, status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLoginView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data["username"]
            password = serializer.validated_data["password"]
            user = user_signup.objects.filter(username=username).first()
            if user and user.check_password(password):
                token, created = Token.objects.get_or_create(user=user)
                return Response({"token": token.key}, status=status.HTTP_200_OK)
            return Response(
                {"error": "Invalid username or password"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileListCreate(generics.ListCreateAPIView):
    queryset = user_Profile.objects.all()
    serializer_class = ProfileSerializer

    def create(self, request, *args, **kwargs):
        user_data = request.data.get("user")
        if user_data:
            user_serializer = UserSignupSerializer(data=user_data)
            if user_serializer.is_valid():
                user = user_serializer.save()
                profile_data = request.data.copy()
                profile_data["user"] = user.id
                profile_serializer = self.get_serializer(data=profile_data)
                if profile_serializer.is_valid():
                    profile_serializer.save()
                    return Response(
                        profile_serializer.data, status=status.HTTP_201_CREATED
                    )
                else:
                    user.delete()
                    return Response(
                        profile_serializer.errors, status=status.HTTP_400_BAD_REQUEST
                    )
            else:
                return Response(
                    user_serializer.errors, status=status.HTTP_400_BAD_REQUEST
                )
        return super().create(request, *args, **kwargs)


class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = user_Profile.objects.all()
    serializer_class = ProfileSerializer
