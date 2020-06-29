from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse_lazy


# creating post model

class Post(models.Model):

    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, blank=True,
                                   related_name='post_likes')

    def __str__(self):
        return self.title

    def get_absolute_url(self):

        # returning user to post detail page after they have made a post

        return reverse_lazy('post-detail', kwargs={'pk': self.pk})

    # returning user to post detail page after they have Liked a post

    def get_like_url(self):
        return reverse_lazy('like-toggle', kwargs={'pk': self.pk})

    def get_like_api_url(self):
        return reverse_lazy('like-api-toggle', kwargs={'pk': self.pk})


class Comment(models.Model):

    post = models.ForeignKey('fourm.Post', on_delete=models.CASCADE,
                             related_name='comments')
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    class Meta:

        ordering = ['-created_date']

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
