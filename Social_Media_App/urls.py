from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import UserCreateView, UserDetailView

urlpatterns = [
    path("api/users/", UserCreateView.as_view(), name="user-create"),
    path("api/users/<int:pk>/", UserDetailView.as_view(), name="user-detail"),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
