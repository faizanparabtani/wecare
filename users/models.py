from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(unique=True)
    is_seeker = models.BooleanField(default=False)
    is_provider = models.BooleanField(default=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


    def __str__(self):
        return f'{self.first_name} {self.last_name}'



class Seeker(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    phone_number = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
    
    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

class Provider(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    phone_number = models.CharField(max_length=20)
    designation = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

