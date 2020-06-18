import django_filters as filters
from django_filters import CharFilter
from .models import Product
from django import forms


class ProductFilter(filters.FilterSet):
    LOWEST_HIGHEST_PRICES = (
        ('ascending', 'Low to high'),
        ('desending', 'high to low'),
    )

    name = filters.CharFilter(lookup_expr='icontains',
                              widget=forms.TextInput(
                                  attrs={'placeholder': 'Search Products'}),
                              )
    lowest_highest_prices = filters.ChoiceFilter(empty_label="Sort By",
                                                 choices=LOWEST_HIGHEST_PRICES, method='filter_by_price')

    class Meta:
        model = Product
        fields = [
            'name',


        ]

    def filter_by_price(self, queryset, name, value):
        expression = 'price' if value == 'ascending' else '-price'
        return queryset.order_by(expression)
