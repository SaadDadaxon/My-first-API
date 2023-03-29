from django.shortcuts import render
from rest_framework import views, status
from rest_framework.response import Response

from .models import Post
from .serializers import PostSerializer


class PostListView(views.APIView):

    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PostCreateView(views.APIView):

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = PostSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class PostDetailView(views.APIView):

    def get(self, request, pk, *args, **kwargs):
        post = Post.objects.get(id=pk)
        serializer = PostSerializer(post)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class PostUpdateView(views.APIView):

    def put(self, request, pk, *args, **kwargs):
        date = request.data
        post = Post.objects.get(id=pk)
        serializer = PostSerializer(data=date, instance=post)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class PostPartialView(views.APIView):

    def patch(self, request, pk, *args, **kwargs):
        date = request.data
        post = Post.objects.get(id=pk)
        serializer = PostSerializer(data=date, instance=post, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class PostDeleteView(views.APIView):

    def delete(self, request, pk, *args, **kwargs):
        post = Post.objects.get(id=pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ListCreate(views.APIView):

    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = PostSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class DetailPutPatchDelete(views.APIView):

    def delete(self, request, pk, *args, **kwargs):
        post = Post.objects.get(id=pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def patch(self, request, pk, *args, **kwargs):
        date = request.data
        post = Post.objects.get(id=pk)
        serializer = PostSerializer(data=date, instance=post, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request, pk, *args, **kwargs):
        date = request.data
        post = Post.objects.get(id=pk)
        serializer = PostSerializer(data=date, instance=post)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get(self, request, pk, *args, **kwargs):
        post = Post.objects.get(id=pk)
        serializer = PostSerializer(post)
        return Response(serializer.data, status=status.HTTP_201_CREATED)







