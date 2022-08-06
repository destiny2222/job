from dataclasses import fields
from pyexpat import model
from django import forms
from .models import Generate


class Generateform(forms.ModelForm):
    class Meta:
        model = Generate
        fields = '__all__'
        

