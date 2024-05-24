from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import UserCreateView, UserDetailView, ProfilePhotoUpdateView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("api/users/", UserCreateView.as_view(), name="user-create"),
    path("api/users/<int:pk>/", UserDetailView.as_view(), name="user-detail"),
    path("api/login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path(
        "api/profile/photo/",
        ProfilePhotoUpdateView.as_view(),
        name="profile_photo_update",
    ),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
