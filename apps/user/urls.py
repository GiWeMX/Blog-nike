from django.urls import path
from .views import *


urlpatterns = [
    path('login/', login_page, name='login'),
    path('logout/', logout_page, name='logout'),
    path('sign-up/', sign_up, name='sign_up'),
    path('profile/<int:pk>/', profile, name='profile'),
    path('change-password/', change_password, name='change-password'),
    
]