from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.forms import PasswordChangeForm, PasswordResetForm, SetPasswordForm
from .models import Profile


class UserRegisterForm(UserCreationForm):

    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('first_name', "last_name", 'username',
                  'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        placeholders = {
            'first_name': 'First Name', "last_name": 'Last Name', 'username': 'username',
            'email': 'email', 'password1': 'password', 'password2': 'repeat password',

        }

        self.fields['first_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            placeholder = f'{placeholders[field]} *'
            self.fields[field].help_text = None
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'form-style-input'
            self.fields[field].label = False


class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('first_name', "last_name", 'username',
                  'email', )

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        placeholders = {
            'first_name': 'First Name', "last_name": 'Last Name', 'username': 'username',
            'email': 'email',

        }

        self.fields['first_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            placeholder = f'{placeholders[field]} *'
            self.fields[field].help_text = None
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'form-style-input'
            self.fields[field].label = False


class UserLoginForm(AuthenticationForm):

    class Meta:
        model = User
        fields = ('username', 'password',)

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        placeholders = {
            'username': 'username',
            'password': 'password',

        }

        self.fields['username'].widget.attrs['autofocus'] = True
        for field in self.fields:
            placeholder = f'{placeholders[field]} *'
            self.fields[field].help_text = None
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'form-style-input'
            self.fields[field].label = False


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'default_phone_number': 'Phone Number',
            'default_postcode': 'Postal Code',
            'default_town_or_city': 'Town or City',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_county': 'County, State or Locality',
        }

        self.fields['default_phone_number'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'default_country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'form-style-input'
            self.fields[field].label = False


class UserPasswordChangeForm(PasswordChangeForm):
    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        placeholders = {
            'old_password': 'Old Password',
            'new_password1': 'New Password',
            'new_password2': 'Confirm new Password',

        }

        self.fields['old_password'].widget.attrs['autofocus'] = True
        for field in self.fields:
            placeholder = f'{placeholders[field]} *'
            self.fields[field].help_text = None
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'form-style-input'
            self.fields[field].label = False


class UserPasswordResetForm(PasswordResetForm):

    class Meta:
        model = User
        fields = ('email',)

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.fields['email'].label = False
        self.fields['email'].widget.attrs['class'] = 'form-style-input'
        self.fields['email'].widget.attrs['placeholder'] = 'Enter Email *'


class UserSetPasswordForm(SetPasswordForm):

    class Meta:
        model = User
        fields = ('new_password1', 'new_password2',)

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        placeholders = {
            'new_password1': 'New Password',
            'new_password2': 'Confirm new Password',

        }

        self.fields['new_password1'].widget.attrs['autofocus'] = True
        for field in self.fields:
            placeholder = f'{placeholders[field]} *'
            self.fields[field].help_text = None
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'form-style-input'
            self.fields[field].label = False
