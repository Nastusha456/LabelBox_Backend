

from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from users.models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        "class": "data",
        "placeholder": "Username"
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "data",
        "placeholder": "Password"
    }))

    class Meta:
        model = User
        fields = ('username', 'password')


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        "class": "data",
        "placeholder": "Username"
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "data",
        "placeholder": "Password"
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "data",
        "placeholder": "Confirm Password"
    }))

    class Meta:
        model = User
        fields = ('username', "password1", "password2")
