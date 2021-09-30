from django.db import models
from django.contrib.auth.models import AbstractUser
from django.shortcuts import reverse
from django.utils import timezone


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
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    phone_number = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
    medicaid_recepient = models.BooleanField(default=False)
    ethnicity = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

    def get_absolute_url(self):
        return reverse('s_profile', kwargs={'pk': self.pk})


class Provider(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    phone_number = models.CharField(max_length=20)
    designation = models.CharField(max_length=20)
    ethnicity = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

    def get_absolute_url(self):
        return reverse('p_profile', kwargs={'pk': self.pk})


class IsConsulting(models.Model):
    seeker = models.ForeignKey(
        Seeker, related_name='seeker', on_delete=models.CASCADE)
    provider = models.ForeignKey(
        Provider, on_delete=models.CASCADE, related_name='provider')
    date_added = models.DateTimeField(default=timezone.now)
    date_removed = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f'{self.seeker} is consulting {self.provider}'
