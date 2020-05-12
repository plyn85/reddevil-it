from django.shortcuts import render
from django.views.generic import ListView
from .models import Post


def home(request):
    context = {
        'posts': Post.objects.all()}
    return render(request, "fourm/home.html", context)


class PostListView(ListView):
    model = Post
    # changing the default page where the list views looks for template
    template_name = 'fourm/home.html'
    context_object_name = "posts"
    ordering = ['-date_posted']
