from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    location = forms.CharField(required=True)
    birth_date = forms.DateField(required=True)
    full_name = forms.CharField()

    class Meta:
        model = User
        fields = ['full_name', 'username', 'email', 'password1',
                  'password2', 'location', 'birth_date']

    # def save(self, commit=True):
    #     user = super(UserCreationForm, self).save(commit=False)
    #     user.location = self.cleaned_data["location"]
    #     user.birth_date = self.cleaned_data["birth_date"]
    #     if commit:
    #         user.save()
    #     return user
