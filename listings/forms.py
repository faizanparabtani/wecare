from django import forms
from .models import Listing


class EditListingForm(forms.ModelForm):

    class Meta:
        model = Listing
        fields = ['description', 'consultation_charges']
