from rest_framework import serializers
from .models import Post, Comment


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.email')

    class Meta:
        model = Post
        fields = ('id', 'title', 'description', 'author', 'text',)


class CommentSerializer(serializers.ModelSerializer):
    post = serializers.ReadOnlyField(source='post.title')

    class Meta:
        model = Comment
        fields = ('id', 'email', 'post', 'text',)