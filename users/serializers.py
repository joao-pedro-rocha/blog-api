#from django.contrib.auth import User
from .models import User
from rest_framework import serializers
from posts.models import Post

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'name', 'age', 'cpf', 'rg', 'phone',)