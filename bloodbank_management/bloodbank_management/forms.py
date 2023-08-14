# forms.py

from django import forms
from bloodbank.models import BloodBank

class DonorForm(forms.ModelForm):
    class Meta:
        model = BloodBank
        fields = ['name', 'location', 'blood_group', 'quantity']
