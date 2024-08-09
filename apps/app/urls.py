from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('post-detail/<int:pk>/', post_detail, name='post_detail'),
    path('post-create/', post_create, name='post_create'),
    path('post-update/<int:pk>/', post_update, name='post_update'),
    path('post-delete/<int:pk>/', post_delete, name='post_delete'),
    path('my_posts/', my_posts, name='my_posts'),
    path('delete_comment/<int:pk>/', delete_comment, name='delete_comment'),
    path('comment_like/<int:pk>/', comment_like, name='comment_like'),
    path('comment_reply/<int:pk>', comment_reply, name='comment_reply')

]