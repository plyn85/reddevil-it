from django import forms
from .models import Comment, Post
from django.views.generic import CreateView
from django.forms import ModelForm, Textarea


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('text',)


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'content',)

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        placeholders = {
            'title': 'Add your post title',
            'content': 'Add your Post content',

        }
        self.fields['title'].widget.attrs['autofocus'] = True
        self.fields['title'].widget.attrs['class'] = 'form-style-input'
        self.fields['content'].widget.attrs['class'] = 'content-form-style-input'
        for field in self.fields:
            self.fields[field].help_text = None
            self.fields[field].widget.attrs['placeholder'] = placeholders[field]
            self.fields[field].label = False


class UpdatePostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'content',)

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        placeholders = {
            'title': 'Add your post title',
            'content': 'Add your Post content',

        }
        self.fields['title'].widget.attrs['autofocus'] = True
        self.fields['title'].widget.attrs['class'] = 'form-style-input'
        self.fields['content'].widget.attrs['class'] = 'content-form-style-input'
        for field in self.fields:
            self.fields[field].help_text = None
            self.fields[field].widget.attrs['placeholder'] = placeholders[field]
            self.fields[field].label = False


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('text',)

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.fields['text'].widget.attrs['autofocus'] = True
        self.fields['text'].widget.attrs['class'] = 'content-form-style-input'
        self.fields['text'].help_text = None
        self.fields['text'].widget.attrs['placeholder'] = 'Add your comment here'
        self.fields['text'].label = False
