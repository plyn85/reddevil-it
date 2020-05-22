from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView,  PostDeleteView, UserPostListView, add_comment_to_post, PostLikeToggle, PostLikeAPIToggle
from django_filters.views import FilterView
from .filters import PostFilter

urlpatterns = [
    path('', PostListView.as_view(), name="fourm-home"),
    # path('search/', search, name='search'),
    path('user/<str:username>', UserPostListView.as_view(), name="user-post"),
    path('post/<int:pk>/like/',
         PostLikeToggle.as_view(), name="like-toggle"),
    path('api/post/<int:pk>/like/',
         PostLikeAPIToggle.as_view(), name="like-api-toggle"),
    path('post/<int:pk>/', PostDetailView.as_view(), name="post-detail"),
    path('post/new/', PostCreateView.as_view(), name="post-create"),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name="post-delete"),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name="post-update"),
    path('post/<int:pk>/comment/', add_comment_to_post,
         name='add_comment_to_post'),
    #     path('comment/<int:pk>/approve/',
    #          comment_approve, name='comment_approve'),
    #     path('comment/<int:pk>/remove/', comment_remove, name='comment_remove'),

]
