from django import forms
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
