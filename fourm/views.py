from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


def home(request):
    context = {
        'posts': Post.objects.all()}
    return render(request, "fourm/home.html", context)

# <app>/<model>_<veiwtype>.html is what django class based views look for by default


class PostListView(ListView):
    # adding post model
    model = Post
    # changing the default page where the list views looks for template
    template_name = 'fourm/home.html'
    context_object_name = "posts"
    ordering = ['-date_posted']


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
