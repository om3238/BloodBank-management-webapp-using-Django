from django import forms
from .models import BloodBank

class BloodBankForm(forms.ModelForm):
    class Meta:
        model = BloodBank
        fields = ['name', 'location', 'blood_group', 'quantity']
