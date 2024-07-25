from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('post-detail/<int:pk>/', post_detail, name='post_detail'),
    path('post-create/', post_create, name='post_create'),
    path('post-update/<int:pk>/', post_update, name='post_update'),
    path('post-delete/<int:pk>/', post_delete, name='post_delete'),

]