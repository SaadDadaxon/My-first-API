from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'image', 'body', 'created_date']

    def validate(self, attrs):
        title = attrs.get('title')
        body = attrs.get('body', None)
        if title.islower():
            raise ValidationError({"title": "First letter of title must be uppercase"})
        if body and len(body) < 10:
            raise ValidationError({"body": "Body must be grater then 10 digits"})
        return attrs

