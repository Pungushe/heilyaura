from django import forms
from .models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm

class UserLoginForm(AuthenticationForm):
     username = forms.CharField()
     password = forms.CharField()

     class Meta:
          model = User
          fields = ['username', 'password']
          
class UserRegistrationForm(UserCreationForm):
     
     class Meta:
          model = User
          fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')
          
          first_name = forms.CharField(label='Имя', widget=forms.TextInput)
          last_name = forms.CharField(label='Фамилия', widget=forms.TextInput)
          username = forms.CharField(label='Имя пользователя', widget=forms.TextInput)
          email = forms.EmailField(label='Электронная почта', widget=forms.EmailInput)
          password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput)
          password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput)
class ProfileForm(UserChangeForm):
     class Meta:
          model = User
          fields = ('image','first_name', 'last_name', 'username', 'email')
          
          image = forms.ImageField(label='Аватар', widget=forms.FileInput, required=False)
          first_name = forms.CharField(label='Имя', widget=forms.TextInput)
          last_name = forms.CharField(label='Фамилия', widget=forms.TextInput)
          username = forms.CharField(label='Имя пользователя', widget=forms.TextInput)
          email = forms.EmailField(label='Электронная почта', widget=forms.EmailInput)
          