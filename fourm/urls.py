
from django.urls import path
from  . views import PostListView, PostCreateView, PostDetailView, \
    PostUpdateView, PostDeleteView, UserPostListView, PostLikeToggle, \
    PostLikeAPIToggle, add_comment_to_post
from django_filters.views import FilterView
from . filters import PostFilter
from . forms import PostForm

urlpatterns = [  
path('', PostListView.as_view(), name='fourm-home'),
    path('user/<str:username>', UserPostListView.as_view(),
         name='user-post'),
    path('post/<int:pk>/like/', PostLikeToggle.as_view(),
         name='like-toggle'),
    path('api/post/<int:pk>/like/', PostLikeAPIToggle.as_view(),
         name='like-api-toggle'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'
         ),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(),
         name='post-delete'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(),
         name='post-update'),
    path('post/<int:pk>/comment/', add_comment_to_post,
         name='add_comment_to_post'),
    ]

    
