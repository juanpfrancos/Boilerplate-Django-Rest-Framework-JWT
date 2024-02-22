from django.urls import path
from .views import create_user, login, current_datetime

urlpatterns = [
    path('users/', create_user),
    path('login/', login),
    path('current_datetime/', current_datetime),
]
