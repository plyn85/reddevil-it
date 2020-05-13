from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserListView

urlpatterns = [
    path('', PostListView.as_view(), name="fourm-home"),
    path('user/<str:username>', UserPostListView.as_view(), name="user-post"),
    path('post/<int:pk>/', PostDetailView.as_view(), name="post-detail"),
    path('post/new/', PostCreateView.as_view(), name="post-create"),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name="post-delete"),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name="post-update"),
]
