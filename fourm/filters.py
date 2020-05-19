import django_filters as filters
from django_filters import CharFilter
from .models import Post


class PostFilter(filters.FilterSet):
    """ taken and altered from a tutorial found at https://www.youtube.com/watch?v=nle3u6Ww6Xktaken """

    # # setting custom lables
    # title = filters.CharFilter(
    #     label="Search Post Titles", lookup_expr='icontains')
    # content = filters.CharFilter(
    #     label="Search Post Content", lookup_expr='icontains')

    CHOICES = (
        ('ascending', 'Oldest Posts'),
        ('desending', 'Newest Posts'),
    )

    ordering = filters.ChoiceFilter(
        label='Search by Date Posted', choices=CHOICES, method='filter_by_order')

    def filter_by_order(self, queryset, name, value):
        expression = 'date_posted' if value == 'ascending' else '-date_posted'
        return queryset.order_by(expression)

    # def __init__(self, *args, **kwargs):
    #     super(PostFilter, self).__init__(*args, **kwargs)
    #     self.filters['title'].label = "Article"
    #     self.filters['content'].label = "Seller"

    class Meta:
        model = Post
        fields = {

            'title': ['icontains'],
            'content': ['icontains'],
        }
