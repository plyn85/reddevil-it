from django.contrib import admin
from .models import Post, Comment


class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'text', 'post', 'created_date', )
    list_filter = ('created_date',)
    search_fields = ('author', 'text')
    # actions = ['approve_comments']


admin.site.register(Comment, CommentAdmin)


class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'content',)
    search_fields = ('author', 'content')
    # actions = ['approve_comments']


admin.site.register(Post, PostAdmin)
