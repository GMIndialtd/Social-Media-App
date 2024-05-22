# urls.p
from django.urls import path
from .views import signup
from .views import UserLoginView, ProfileListCreate, ProfileDetail

urlpatterns = [
    path("signup/", signup, name="signup"),
    path("login/", UserLoginView.as_view(), name="login"),
    path('profiles/', ProfileListCreate.as_view(), name='profile-list-create'),
    path('profiles/<int:pk>/', ProfileDetail.as_view(), name='profile-detail'),
]
