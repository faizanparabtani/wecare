from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.db import transaction
from .models import User, Seeker, Provider

class SeekerSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    phone_number = forms.CharField(required=True)
    location = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'phone_number', 'location']
    
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_seeker = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.save()
        seeker = Seeker.objects.create(user=user)
        seeker.phone_number=self.cleaned_data.get('phone_number')
        seeker.location=self.cleaned_data.get('location')
        seeker.save()
        return user

class ProviderSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    phone_number = forms.CharField(required=True)
    designation = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'phone_number', 'designation']

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_provider = True
        user.is_staff = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.save()
        provider = Provider.objects.create(user=user)
        provider.phone_number=self.cleaned_data.get('phone_number')
        provider.designation=self.cleaned_data.get('designation')
        provider.save()
        return user