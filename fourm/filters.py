import django_filters as filters
from django_filters import CharFilter
from .models import Post, Comment
from django.db.models import Q


class PostFilter(filters.FilterSet):
    """ taken and altered from a tutorial found at https://www.youtube.com/watch?v=nle3u6Ww6Xktaken """

    CHOICES = (
        ('ascending', 'Oldest Posts'),
        ('desending', 'Newest Posts'),
    )
    # setting custom labels and filters
    title = filters.CharFilter(
        label="Search Post Titles", lookup_expr='icontains')
    content = filters.CharFilter(
        label="Search Post content", lookup_expr='icontains')
    # author = filters.CharFilter(
    #     label="Search Post author")
    multi_name_fields = filters.CharFilter(
        label="Search by post title, post content", method='filter_by_multiple_fields')
    ordering = filters.ChoiceFilter(
        label='Search by Newest/Oldest', choices=CHOICES, method='filter_by_order')

    class Meta:
        model = Post
        fields = [

        ]

    def filter_by_order(self, queryset, name, value):
        expression = 'date_posted' if value == 'ascending' else '-date_posted'
        return queryset.order_by(expression)

    def filter_by_multiple_fields(self, queryset, name, value):
        return Post.objects.filter(
            Q(title__icontains=value) | Q(
                content__icontains=value)

        )


class Commentsfilter(filters.FilterSet):

    # setting custom labels and filters
    text = filters.CharFilter(
        label="Search Comments", lookup_expr='icontains')

    class Meta:
        model = Post
        fields = [

        ]
