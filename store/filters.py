import django_filters as filters
from django_filters import CharFilter
from .models import Product
from django import forms


class ProductFilter(filters.FilterSet):

    name = filters.CharFilter(lookup_expr='icontains',
                              widget=forms.TextInput(
                                  attrs={'placeholder': 'Search Products'}),
                              )

    class Meta:
        model = Product
        fields = [
            'name',


        ]
