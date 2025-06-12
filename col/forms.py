from django import forms
from . import models 

class validate(forms.ModelForm):
    class Meta:
        model = models.col
        fields = ['firstname','lastname','age','branch']
