from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Post


class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'image', 'body', 'created_date']

    def validate(self, attrs):
        title = attrs.get('title')

        if title.islower():
            raise ValidationError({"title": "First letter of title must be uppercase"})
        return attrs

