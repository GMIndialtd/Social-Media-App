from django.db import models


# Create your models here.
class user_signup(models.Model):
    fullname = models.CharField(max_length=255)
    username = models.CharField(max_length=50, unique=True, null=False, blank=False)
    email = models.EmailField(max_length=100, unique=True, null=False, blank=False)
    password = models.CharField(max_length=255, null=False, blank=False)
    created_on = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    updated_on = models.DateTimeField(auto_now=True, null=False, blank=False)

    def __str__(self):
        return self.username
    
class user_Profile(models.Model):
    user = models.OneToOneField(user_signup, on_delete=models.CASCADE, related_name='profile')
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    mobile_number = models.CharField(max_length=15)
    profile_image = models.CharField(max_length=255, blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.username} Profile'
