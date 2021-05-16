from django import forms
from .models import HealthData


class AddHealthData(forms.ModelForm):
    class Meta:
        model = HealthData
        fields = ['heartrate', 'steps', 'weight', 'blood_pressure']
