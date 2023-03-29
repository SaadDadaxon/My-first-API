from django.urls import path
from .views import PostListView, PostCreateView, PostDetailView, PostUpdateView, PostPartialView, PostDeleteView, \
    ListCreate, DetailPutPatchDelete

urlpatterns = [
    path('list/', PostListView.as_view()),
    path('post/', PostCreateView.as_view()),
    path('detail/<int:pk>/', PostDetailView.as_view()),
    path('update/<int:pk>/', PostUpdateView.as_view()),
    path('partial/<int:pk>/', PostPartialView.as_view()),
    path('delete/<int:pk>/', PostDeleteView.as_view()),


    path('list-create/', ListCreate.as_view()),
    path('ppdd/<int:pk>/', DetailPutPatchDelete.as_view()),
]
