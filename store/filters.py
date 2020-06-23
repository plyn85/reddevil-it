import django_filters as filters
from django_filters import CharFilter
from .models import Product
from django import forms


class ProductFilter(filters.FilterSet):

    # for price filter
    LOWEST_HIGHEST_PRICES = (
        ('ascending', 'Low to high'),
        ('desending', 'high to low'),
    )

    lowest_highest_prices = filters.ChoiceFilter(empty_label="Sort By",
                                                 choices=LOWEST_HIGHEST_PRICES, method='filter_by_price')

    def filter_by_price(self, queryset, name, value):
        expression = 'price' if value == 'ascending' else '-price'
        return queryset.order_by(expression)

    class Meta:
        model = Product
        fields = ['sizes', 'condtion', 'players_names', 'year', ]
