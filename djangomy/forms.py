from django import forms
from .models import *

class NameForms(forms.ModelForm):
    class Meta:
        model = Subscribers
        exclude = ['']
