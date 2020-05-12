from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post


def home(request):
    context = {
        'posts': Post.objects.all()}
    return render(request, "fourm/home.html", context)

# <app>/<model>_<veiwtype>.html is what django class based views look for by default


class PostListView(ListView):
    model = Post
    # changing the default page where the list views looks for template
    template_name = 'fourm/home.html'
    context_object_name = "posts"
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post
