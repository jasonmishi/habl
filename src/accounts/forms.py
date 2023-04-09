from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, help_text="First Name")
    last_name = forms.CharField(max_length=100, help_text="Last Name")
    username = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=200)

    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        )
