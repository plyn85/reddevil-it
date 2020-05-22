from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth.models import User
# creating post model


class Post(models.Model):

    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, blank=True, related_name="post_likes")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # returning user to post detail page after they have made a post
        return reverse('post-detail', kwargs={'pk': self.pk})
    # counting the posts of each user

    # def count_posts_of(user):
    #     return Post.objects.filter(author=user).count()
    def get_like_url(self):
        return reverse('like-toggle', kwargs={'pk': self.pk})


class Comment(models.Model):
    post = models.ForeignKey(
        'fourm.Post', on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_date', ]

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
