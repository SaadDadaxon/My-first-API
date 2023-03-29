from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PostSerializers
from .models import Post


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializers


