import django_filters as filters
from django_filters import CharFilter
from .models import Product
from django import forms
from django.db.models import Q
import datetime

class ProductFilter(filters.FilterSet):
    """ filter for products used on the product model 
    and render on the products page filter methods for highest and lowest
    prices and for player names, descrption, name and condtion of product
    """

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
    #  filter for sizes

    SIZE_CHOICES = [
        ("S", 'SM'),
        ('M', 'M'),
        ('L', 'L'),
        ( 'XL', 'XL'),
    ]
    sizes = filters.ChoiceFilter(empty_label="By Size",
                                                 choices=SIZE_CHOICES,)    
    
    #  filter for year

    YEAR_CHOICES = []
    for r in range(1991, (datetime.datetime.now().year+1)):
        YEAR_CHOICES.append((r, r))

    year = filters.ChoiceFilter(empty_label="by Year",
                                                 choices=YEAR_CHOICES,)    

     #  filter for shirt condtion      
    SHIRT_CONDTION = [
        ("brand new", 'Brand new'),
        ("Excellent", 'Excellent'),
        ('Mint', 'Mint'),
        ('Very good', 'Very good'),
        ('Good', 'Good'),

    ]

    condtion = filters.ChoiceFilter(empty_label="By Condtion",
                                                 choices= SHIRT_CONDTION,)    

    #  filter for player names      
    PLAYERS_NAMES = [
        ("Giggs", "Giggs"),
        ("Schmeichel", "Schmeichel"),
        ('Beckham', 'Beckham'),
        ('C Ronaldo', 'C Ronaldo'),
        ('Cantona', 'Cantona'),
        ("Rooney", "Rooney"),
        ("Keane", "Keane"),
        ("Scholes", "Scholes"),

    ]    

    players_names = filters.ChoiceFilter(empty_label="By Player",
                                                 choices= PLAYERS_NAMES,)                                         