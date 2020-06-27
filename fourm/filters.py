import django_filters as filters
from django_filters import CharFilter
from .models import Post
from users.models import User
from django.db.models import Q
from django import forms


class PostFilter(filters.FilterSet):
    """ filters for all dropdown menus on shop page """

    class Meta:
        model = Post
        fields = [
            'content', ]
    # setting choices for new/most popular
    NEW_MOST_POP_CHOICES = (
        ('descending', 'Newest Posts'),
        ('likes', 'Most popular Posts'),
    )

    content = filters.CharFilter(lookup_expr='icontains',
                                 widget=forms.TextInput(
                                     attrs={'placeholder': 'Search content'}),
                                 )

    author__username = filters.CharFilter(lookup_expr='icontains',
                                          widget=forms.TextInput(
                                              attrs={'placeholder': 'Search Users'}),)

    new_most_pop_ordering = filters.ChoiceFilter(empty_label="Sort By",
                                                 label='Search by Newest/Most popular', choices=NEW_MOST_POP_CHOICES, method='filter_by_new_most_pop')

    def filter_by_new_most_pop(self, queryset, name, value):
        expression = 'date_posted' if value == 'descending' else '-likes'
        return queryset.order_by(expression)
