from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from .models import Post
from rest_framework.decorators import api_view
from .serializers import PostSerializers, PostCreateSerializers
from rest_framework import status


@api_view(['GET'])
def post_list_1(request):
    posts = Post.objects.all()
    data = []
    for i in posts:
        post = {
            'id': i.id,
            'title': i.title,
            'body': i.body,
            'image': i.get_absolute_url,
            'created_date': i.created_date,
        }
        data.append(post)

    return Response(data)


@api_view(['GET'])
def post_list(request):
    posts = Post.objects.all()
    serializers = PostSerializers(posts, many=True)

    return Response(serializers.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def post_detail(request, pk):
    try:
        posts = Post.objects.get(id=pk)
    except Post.DoesNotExist:
        raise NotFound('Topilmadi')
    serializers = PostSerializers(posts)

    return Response(serializers.data, status=status.HTTP_200_OK)


@api_view(['DELETE'])
def post_delete(request, pk):
    try:
        posts = Post.objects.get(id=pk)
    except Post.DoesNotExist:
        raise NotFound('Topilmadi')
    posts.delete()

    return Response({'detail': 'successfully deleted'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def post_post(request):
    data = request.data
    serializers = PostCreateSerializers(data=data)
    if serializers.is_valid():
        serializers.save()
        return Response(serializers.data, status=status.HTTP_201_CREATED)
    return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def post_update(request, pk):
    try:
        instance = Post.objects.get(id=pk)
    except Post.DoesNotExist:
        raise NotFound('Topilmadi')
    data = request.data
    serializers = PostCreateSerializers(instance, data=data)
    serializers.is_valid(raise_exception=True)
    serializers.save()
    return Response(serializers.data, status=status.HTTP_201_CREATED)


@api_view(['PATCH'])
def post_update_partial(request, pk, **kwargs):
    try:
        instance = Post.objects.get(id=pk)
    except Post.DoesNotExist:
        raise NotFound('Topilmadi')
    data = request.data
    partial = kwargs['partial'] = True
    serializers = PostCreateSerializers(instance, data=data, partial=partial)
    serializers.is_valid(raise_exception=True)
    serializers.save()
    return Response(serializers.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'POST'])
def list_create(request):
    if request.method == "GET":
        posts = Post.objects.all()
        serializers = PostSerializers(posts, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)

    data = request.data
    serializers = PostCreateSerializers(data=data)
    serializers.is_valid(raise_exception=True)
    serializers.save()
    return Response(serializers.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PATCH', 'PUT', 'DELETE'])
def list_rud(request, pk, **kwargs):
    try:
        instance = Post.objects.get(id=pk)
    except Post.DoesNotExist:
        raise NotFound('Topilmadi')
    data = request.data

    if request.method == "GET":
        posts = Post.objects.all()
        serializers = PostSerializers(posts, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)

    if request.method == "PATCH":
        partial = kwargs['partial'] = True
        serializers = PostCreateSerializers(instance, data=data, partial=partial)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response(serializers.data, status=status.HTTP_201_CREATED)

    if request.method == "PUT":
        serializers = PostCreateSerializers(instance, data=data)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response(serializers.data, status=status.HTTP_201_CREATED)

    if request.method == "DELETE":
        instance.delete()

        return Response({'detail': 'successfully deleted'}, status=status.HTTP_204_NO_CONTENT)


