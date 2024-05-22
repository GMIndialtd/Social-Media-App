# urls.p
from django.urls import path
from .views import signup
from .views import UserLoginView

urlpatterns = [
    path("signup/", signup, name="signup"),
    path("login/", UserLoginView.as_view(), name="login"),
]
