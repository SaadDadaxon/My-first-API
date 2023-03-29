from rest_framework import serializers
from .models import Post


class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'get_absolute_url', 'body', 'created_date']


class PostCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'image', 'body', 'created_date']
