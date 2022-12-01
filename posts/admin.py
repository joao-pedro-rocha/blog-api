from django.contrib import admin
from .models import Post, Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'text',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('email', 'post', 'text', 'likes',)


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
