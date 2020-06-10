from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):

    username = forms.CharField(
        max_length=50, required=True, help_text='Requried. No more then 50 characters')
    full_name = forms.CharField(
        max_length=30, required=False, help_text='Optional.')
    password1 = forms.CharField(
        label="password", help_text='At least 8 charcters.')

    email = forms.EmailField(
        max_length=254, help_text='Required. Provide a valid email address.')

    class Meta:
        model = User
        fields = ['full_name', 'username',
                  'email', ]


class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username',
                  'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
