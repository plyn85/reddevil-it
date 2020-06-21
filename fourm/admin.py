from django.contrib import admin
from .models import Post, Comment

admin.site.register(Post)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'text', 'post', 'created_date', )
    list_filter = ('created_on')
    search_fields = ('author', 'text')
    # actions = ['approve_comments']


admin.site.register(Comment)
