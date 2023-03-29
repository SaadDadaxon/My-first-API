from django.urls import path
from .views import post_list, post_detail, post_post, post_update, post_update_partial, list_create, post_delete, \
    list_rud

urlpatterns = [
    path('list/', post_list),
    path('detail/<int:pk>/', post_detail),
    path('create/', post_post),
    path('update/<int:pk>/', post_update),
    path('delete/<int:pk>/', post_delete),
    path('update/partial/<int:pk>/', post_update_partial),


    path('list-create/', list_create),
    path('rud/<int:pk>/', list_rud), 


]
