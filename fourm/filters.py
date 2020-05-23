import django_filters as filters
from django_filters import CharFilter
from .models import Post, Comment
from users.models import User
from django.db.models import Q


class PostFilter(filters.FilterSet):
    """ taken and altered from a tutorial found at https://www.youtube.com/watch?v=nle3u6Ww6Xktaken """
# setting choices for new/old ordering
    NEW_OLD_CHOICES = (
        ('ascending', 'Oldest Posts'),
        ('desending', 'Newest Posts'),
    )
    # setting choices for new/most popular
    NEW_MOST_POP_CHOICES = (
        ('descending', 'Newest Posts'),
        ('likes', 'Most popular Posts'),
    )
    # setting custom labels and filters
    title = filters.CharFilter(
        label="Search Post Titles", lookup_expr='icontains')
    # comments__text = filters.CharFilter(
    #     label="Search Comments")

    content = filters.CharFilter(
        label="Search Post content", lookup_expr='icontains')

    author__username = filters.CharFilter(
        label="Search Post author")

    multi_name_fields = filters.CharFilter(
        label="Search by post title, post content", method='filter_by_multiple_fields')

    new_old_ordering = filters.ChoiceFilter(
        label='Search by Newest/Oldest/ Most Popular', choices=NEW_OLD_CHOICES, method='filter_by_order')

    new_most_pop_ordering = filters.ChoiceFilter(
        label='Search by Newest/Most popular', choices=NEW_MOST_POP_CHOICES, method='filter_by_new_most_pop')

    class Meta:
        model = Post
        fields = [

        ]

    def filter_by_order(self, queryset, name, value):
        expression = 'date_posted' if value == 'ascending' else '-date_posted'
        return queryset.order_by(expression)

    def filter_by_new_most_pop(self, queryset, name, value):
        expression = 'date_posted' if value == 'descending' else '-likes'
        return queryset.order_by(expression)

    def filter_by_multiple_fields(self, queryset, name, value):
        return Post.objects.filter(
            Q(title__icontains=value) | Q(
                content__icontains=value)

        )


# class CommentsFilter(filters.FilterSet):

#     # setting custom labels and filters
#     comments = filters.CharFilter(
#         label="Search Comments")

#     class Meta:
#         model = Comment
#         fields = [

#         ]
