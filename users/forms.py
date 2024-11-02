from django import forms
from .models import User
from django.contrib.auth.forms import AuthenticationForm

class UserLoginForm(AuthenticationForm):
     username = forms.CharField(label='Имя пользователя', widget=forms.TextInput)
     password = forms.CharField(label='Пароль', widget=forms.PasswordInput)

     class Meta:
          model = User
          fields = ['username', 'password']