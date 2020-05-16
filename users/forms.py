from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(
        max_length=50, required=True, help_text='Requried. No more then 50 characters')
    first_name = forms.CharField(
        max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(
        max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(
        max_length=254, help_text='Required. Provide a valid email address.')
    birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')
    location = forms.CharField(
        max_length=30, required=True, help_text='Required.')

    class Meta:
        model = User
        fields = ('username',  'first_name', 'last_name',
                  'email', 'password1', 'password2', 'location', 'birth_date',)
