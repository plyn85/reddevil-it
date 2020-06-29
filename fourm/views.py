from rest_framework.views import APIView
from rest_framework import authentication, permissions
from rest_framework.response import Response
from . models import Post
from . forms import CommentForm, PostForm
from django.views.generic import ListView, DetailView, CreateView, \
    UpdateView, DeleteView, RedirectView
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, \
    UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from . filters import PostFilter
from store.models import Product
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin


def home(request):
    """ function renders home view """

    return render(request, 'fourm/home.html', context)


@login_required
def add_comment_to_post(request, pk):
    """from a tutorial at https://tutorial-extensions.djangogirls.org/en/
homework_create_more_models/ if its a post method saves the comment
form with post attached an returns user to post detail page if its a 
get request rensers comment form on add_comment_to_post page"""

    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            messages.success(request,
                             'Your comment was added succesfully')
            return redirect('post-detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'fourm/add_comment_to_post.html',
                  {'form': form})


class FilteredListView(ListView):

    """added from a tutorial found at https://www.caktusgroup.com/blog/
    2018/10/18/filtering-and-pagination-django/ used to allow django-filters 
    to be used with class based views used on  the PostList view below """

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
        # Pass the filterset to the template - it provides the form
        context['filterset'] = self.filterset
        return context


class PostListView(FilteredListView):

    """ renders all posts on the fourm home page using post model in 
    reverse order by date posted paginted so 5 posts shown at a 
    time, filterlistview passed in from above to allow django
    filters postfilter to be filterset class passed into the 
    fourm home page  """

    # filterset_class = CommentsFilter
    filterset_class = PostFilter
    # adding post model
    model = Post
    # changing the default page where the list views looks for template
    template_name = 'fourm/home.html'
    context_object_name = "posts"
    ordering = ['-date_posted']
    paginate_by = 5


class PostLikeToggle(RedirectView):

    """ from a tutorial at https://www.youtube.com/watch?v=pkPRtQf6oQ8&t=678s This view gets the object adds the like and returns back to the detail view used on the post_detail """

    def get_redirect_url(self, *args, **kwargs):
        # getting the post object of each post
        obj = get_object_or_404(Post, pk=kwargs['pk'])
    #     getting the url of the post
        url_ = obj.get_absolute_url()
        # getting current user
        user = self.request.user
        # authenticating  user
        if user.is_authenticated:
            # if the user has already liked post remove
            if user in obj.likes.all():
                obj.likes.remove(user)
            else:
                obj.likes.add(user)

            return url_


class PostLikeAPIToggle(APIView):

    """from a tutorial at https://www.youtube.com/watch?v=pkPRtQf6oQ8&t=678s 
    genric api view used from django rest framework to handle like down vote functionallity"""

    def get(self, request, *args, **kwargs):
        # getting post object
        obj = get_object_or_404(Post, pk=kwargs['pk'])

        url_ = obj.get_absolute_url()
        user = self.request.user
        updated = False
        liked = False
        # if the user is a logged in user
        if user.is_authenticated:
            # if the user has already liked a post
            if user in obj.likes.all():
                liked = False
                obj.likes.remove(user)
        # if ther user hasn, t liked the post
            else:
                liked = True
                obj.likes.add(user)
                updated = True
            data = {
                "updated": updated,
                "liked": liked
            }

            return Response(data)


class UserPostListView(ListView):

    """user  post list view displays all posts form a user
       with only posts showing per page pagination used """

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

    """post detail view displays each post in a detail view"""

    # adding post model
    model = Post


class PostCreateView(SuccessMessageMixin, LoginRequiredMixin,
    CreateView):

    """ post create view displays post form where the user can create 
        a post """

    # adding post model
    model = Post
    # adding post form
    form_class = PostForm
    success_message = "Your Post was created successfully"

# overiding the from valid method here

    def form_valid(self, form):
        # setting author to current logged In user
        form.instance.author = self.request.user
        # runnig the form
        return super().form_valid(form)


class PostUpdateView(SuccessMessageMixin, LoginRequiredMixin,
    UserPassesTestMixin, UpdateView):

    """ view allows the user to update a post they already 
        created"""

    # adding post model
    model = Post
    # only taking title and content fields from post model
    form_class = PostForm
    success_message = "Your Post was Updated successfully"
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


class PostDeleteView(SuccessMessageMixin, LoginRequiredMixin,
    UserPassesTestMixin, DeleteView):

    """ view allows user to delete the own posts"""

    # adding post model
    model = Post
    # adding route to home page after post Is deleted
    success_url = "/"
    success_message = "Your Post was Deleted successfully"
    # adding test function so user can only update there own posts

    def test_func(self):
        # getting current post
        post = self.get_object()
        # checking if currenty user is the author of the post
        if self.request.user == post.author:
            return True
        return False