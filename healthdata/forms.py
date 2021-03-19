from django import forms
from .models import HealthData


class AddHealthData(forms.ModelForm):
    # phone_number = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'placeholder': 'TestSeeker'}), required=False)
    # designation = forms.CharField(max_length=20, required=False)

    class Meta:
        model = HealthData
        fields = ['heartrate', 'steps', 'weight']
