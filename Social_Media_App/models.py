from django.db import models
# from django.contrib.auth.models import User


# Create your models here.
class user_signup(models.Model):
    username = models.CharField(max_length=50, unique=True, null=False, blank=False)
    email = models.EmailField(max_length=100, unique=True, null=False, blank=False)
    password = models.CharField(max_length=255, null=False, blank=False)
    created_on = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    updated_on = models.DateTimeField(auto_now=True, null=False, blank=False)

    def __str__(self):
        return self.username


class UserProfile(models.Model):
    user = models.OneToOneField(
        user_signup, on_delete=models.CASCADE, related_name="profile"
    )
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    mobile_number = models.CharField(max_length=15, null=True, blank=True)
    profile_image = models.ImageField(
        upload_to="profile_images/", null=True, blank=True
    )
    cover_photo = models.ImageField(upload_to="cover_photos/", null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    interests = models.TextField(null=True, blank=True)
    contact_info = models.TextField(null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username
