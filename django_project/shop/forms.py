from django import forms
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User

class RegisterUserForm(UserCreationForm):
  username = forms.CharField(
                widget=forms.TextInput(attrs={
                                          'class': 'input-field',
                                          'placeholder': 'Логин',
                                        }),
                )
  password1 = forms.CharField(
                widget=forms.PasswordInput(attrs={
                                          'class': 'input-field',
                                          'placeholder': 'Пароль',
                                        }),
                )
  password2 = forms.CharField(
                widget=forms.PasswordInput(attrs={
                                          'class': 'input-field',
                                          'placeholder': 'Повторите пароль',
                                        }),
                )
  
  class Meta:
    model = User
    fields = ('username', 'password1', 'password2')
    widgets = {
      'username': forms.TextInput(attrs={
                                          'class': 'input-field',
                                          'placeholder': 'Логин',
                                        }),
      'password1': forms.PasswordInput(attrs={
                                          'class': 'input-field',
                                          'placeholder': 'Пароль',
                                        }),
      'password2': forms.PasswordInput(attrs={
                                          'class': 'input-field',
                                          'placeholder': 'Повторите пароль',
                                        }),   
    }