from django import forms
from .models import Comments

lass CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)
