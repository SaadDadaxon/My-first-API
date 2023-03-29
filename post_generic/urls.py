from django.urls import path
from .views import PostListView, PostCreateView, PostRetrieveView, PostDeleteView, PostUpdateView, PostListCreateView, PostRUDView

urlpatterns = [
    path('list/', PostListView.as_view()),
    path('create/', PostCreateView.as_view()),
    path('retrieve/<int:pk>/', PostRetrieveView.as_view()),
    path('delete/<int:pk>/', PostDeleteView.as_view()),
    path('update/<int:pk>/', PostUpdateView.as_view()),
    path('rud/<int:pk>/', PostRUDView.as_view()),
    path('list-create/', PostListCreateView.as_view()),
]
