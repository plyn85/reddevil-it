from django.test import TestCase
from .forms import PostForm,CommentForm

class TestPostForm(TestCase):

    def test_post_title(self):
        form = PostForm({'title':'test'})
        self.assertFalse(form.is_valid())
    

    def test_post_content(self):
        form = PostForm({'content':'test'})
        self.assertFalse(form.is_valid())

class TestCommentForm(TestCase):

    def test_comment_text(self):
        form = PostForm({'text':'test'})
        self.assertFalse(form.is_valid())
    

    