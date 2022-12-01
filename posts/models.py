from django.db import models
from users.models import User

class Post(models.Model):
    author = models.ForeignKey(User, verbose_name='Autor', null=True,
                               on_delete=models.CASCADE)
    title = models.CharField(verbose_name='Título', max_length=100)
    description = models.CharField(verbose_name='Descrição', max_length=200,
                                   null=True, blank=True)
    text = models.TextField(verbose_name='Texto')

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

class Comment(models.Model):
    email = models.EmailField(verbose_name='Email', null=True)
    post = models.ForeignKey(Post, verbose_name='Post',
                             on_delete=models.CASCADE)
    text = models.TextField(verbose_name='Texto', )
    likes = models.IntegerField(verbose_name='Likes', default=0, null=True)

    class Meta:
        ordering = ['post']

    def increment_likes(self):
        self.likes += 1
        self.save()

    def __str__(self):
        return f'{self.post}'
