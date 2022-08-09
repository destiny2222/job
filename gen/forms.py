from dataclasses import fields
from pyexpat import model
from django import forms
from .models import Generate,PaymentSlip


class Generateform(forms.ModelForm):
    class Meta:
        model = Generate
        fields = '__all__'

class Slip(forms.ModelForm):
    class Meta:
        model = PaymentSlip
        fields = '__all__'
        

