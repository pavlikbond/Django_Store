from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Your Username',
               'class': 'w-full py-2 px-4 rounded'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Your Password',
               'class': 'w-full py-2 px-4 rounded'}))


class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )

    username = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Your Username',
               'class': 'w-full py-2 px-4 rounded'}))
    email = forms.CharField(widget=forms.EmailInput(
        attrs={'placeholder': 'Your Email',
               'class': 'w-full py-2 px-4 rounded'}))
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Your Password',
               'class': 'w-full py-2 px-4 rounded'}))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Repeat Password',
               'class': 'w-full py-2 px-4 rounded'}))
