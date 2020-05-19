from .models import Post, Comment
from .forms import CommentForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Q
from .filters import PostFilter


def home(request):
    # post_count = Post.objects.filter(author=request.user).count()
    posts = Post.objects.all()
    posts = my_filter.qs
    context = {
        # 'post_count': post_count,
        'posts': posts}
    return render(request, "fourm/home.html", context)

# <app>/<model>_<veiwtype>.html is what django class based views look for by default


class FilteredListView(ListView):
    """added from a tutorial found at https://www.caktusgroup.com/blog/2018/10/18/filtering-and-pagination-django/"""

    filterset_class = None

    def get_queryset(self):
        # getting the query set
        queryset = super().get_queryset()
        # then using the parameters to instantiate the filter set
        self.filterset = self.filterset_class(
            self.request.GET, queryset=queryset)
        # returning the filtered queryset
        return self.filterset.qs.distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Pass the filterset to the template - it provides the form.
        context['filterset'] = self.filterset
        return context


class PostListView(FilteredListView):
    filterset_class = PostFilter

    # adding post model
    model = Post
    # changing the default page where the list views looks for template
    template_name = 'fourm/home.html'
    context_object_name = "posts"
    ordering = ['-date_posted']
    paginate_by = 5


class UserPostListView(ListView):
    # adding post model
    model = Post
    # changing the default page where the list views looks for template
    template_name = 'fourm/user_posts.html'
    context_object_name = "posts"
    paginate_by = 5
# overriding the method an changing the query set here

    def get_queryset(self):
        # capturing user In user variable If It exists
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        # filtering posts by user
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    # adding post model
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    # adding post model
    model = Post
    # only taking title and content fields from post model
    fields = ['title', 'content']
# overiding the from valid method here

    def form_valid(self, form):
        # setting author to current logged In user
        form.instance.author = self.request.user
        # runnig the form
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    # adding post model
    model = Post
    # only taking title and content fields from post model
    fields = ['title', 'content']
# overiding the from valid method here

    def form_valid(self, form):
        # setting author to current logged In user
        form.instance.author = self.request.user
        # runnig the form
        return super().form_valid(form)

    # adding test function so user can only update there own posts

    def test_func(self):
        # getting current post
        post = self.get_object()
        # checking if currenty user is the author of the post
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    # adding post model
    model = Post
    # adding route to home page after post Is deleted
    success_url = "/"

    # adding test function so user can only update there own posts

    def test_func(self):
        # getting current post
        post = self.get_object()
        # checking if currenty user is the author of the post
        if self.request.user == post.author:
            return True
        return False


@login_required
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post-detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'fourm/add_comment_to_post.html', {'form': form})


# @login_required
# def comment_approve(request, pk):
#     comment = get_object_or_404(Comment, pk=pk)
#     comment.approve()
#     return redirect('post-detail', pk=comment.post.pk)


# @login_required
# def comment_remove(request, pk):
#     comment = get_object_or_404(Comment, pk=pk)
#     comment.delete()
#     return redirect('post-detail', pk=comment.post.pk)


# def approved_comments(self):
#     return self.comments.filter(approved_comment=True)
