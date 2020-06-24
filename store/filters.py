import django_filters as filters
from django_filters import CharFilter
from .models import Product
from django import forms
from django.db.models import Q


class ProductFilter(filters.FilterSet):

    class Meta:
        model = Product
        fields = ['sizes', 'condtion', 'players_names', 'year', ]

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

    search_all_products = filters.CharFilter(method='filter_all', widget=forms.TextInput(
        attrs={'placeholder': 'Search All Products'},))

    def filter_all(self, queryset, name, value):
        return Product.objects.filter(
            Q(name__icontains=value) | Q(description__icontains=value)
            | Q(condtion__icontains=value) | Q(players_names__icontains=value)

        )
