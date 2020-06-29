from django.contrib import admin
from .models import Post, Comment


class CommentAdmin(admin.ModelAdmin):
    list_display = ('text', 'post', 'created_date', )
    list_filter = ('created_date',)
    search_fields = ('text',)
    # actions = ['approve_comments']


admin.site.register(Comment, CommentAdmin)


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content',)
    search_fields = ('content',)
    # actions = ['approve_comments']


admin.site.register(Post, PostAdmin)
