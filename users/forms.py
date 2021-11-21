from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
# from .models import Profile
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV3
from django.contrib.auth.forms import AuthenticationForm
import datetime


class UserRegisterForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)

        # for fieldname in ['username', 'password1', 'password2']:
        self.fields['password1'].help_text = 'Please keep your password dissimilar from your other info, 8 Characterers Minium, Not entirely Numeric, also please don\'t use common passwords for security purposes'
    email = forms.EmailField()

    def clean(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError(
                "Entered Email already exists ! Please Login")
        return self.cleaned_data

    captcha = ReCaptchaField(
        label='',
        widget=ReCaptchaV3(
            attrs={
                'required_score': 0.75,
            }
        )
    )

    class Meta:
        model = User
        fields = ['username', 'email',  'password1', 'password2']

class UserLoginForm(AuthenticationForm):
    captcha = ReCaptchaField(
        label='',
        widget=ReCaptchaV3(
            attrs={
                'required_score': 0.75,
            }
        )
    )

    class Meta:
        fields = ['username', 'password', 'captcha']
