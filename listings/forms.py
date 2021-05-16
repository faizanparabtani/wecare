from django import forms
from django.db.models import fields
from .models import Listing
from users.models import IsConsulting


class EditListingForm(forms.ModelForm):

    class Meta:
        model = Listing
        fields = ['description', 'consultation_charges']


class AddSeekerForm(forms.ModelForm):

    class Meta:
        model = IsConsulting
        fields = ['seeker']


class RemoveSeekerForm(forms.ModelForm):
    class Meta:
        model = IsConsulting
        fields = ['seeker']
