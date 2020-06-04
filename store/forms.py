from django import forms
from . models import Customer


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('full_name', 'email', 'phone_number')

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',

        }
