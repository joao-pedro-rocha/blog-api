from django.shortcuts import render, redirect
from users.models import User

from .models import Post, Comment
from .forms import CommentForm
from .permissions import IsOwnerOrReadOnly

from rest_framework import generics, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .serializers import PostSerializer, CommentSerializer

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('users-api-list', request=request, format=format),
        'posts': reverse('posts-api-list', request=request, format=format),
        'comments': reverse('comments-api-list', request=request,
                            format=format)
    })


def post_list(request):
    posts = Post.objects.all()

    return render(request, 'posts/post_list.html', locals())


def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    comments = Comment.objects.filter(post=post)
    new_comment = None
    
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, 'posts/post_detail.html', locals())


class PostAPIList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user.email)


class PostAPIDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)


class CommentAPIList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentAPIDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


def like(request, comment_id, post_id):
    post = Post.objects.get(id=post_id)
    comment = Comment.objects.get(id=comment_id)
    comment.increment_likes()

    return redirect('post-detail', post.id)

