from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from users.models import User
from django import forms

class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']