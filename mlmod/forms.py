from django import forms
from .models import ModelCall

class MLCallImageForm(forms.ModelForm):
    class Meta:
        model = ModelCall
        fields = ['image']

        labels = {
            'image': 'image'
        }