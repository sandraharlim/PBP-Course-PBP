from django.urls import path
from django.urls.conf import include
from .views import todo_index, todo_detail, todo_delete, json, from_dart
from rest_framework import routers



urlpatterns = [
    path('', todo_index, name='index'),
    path('todo-delete/', todo_delete, name='todo_delete'),
    path('<id>/todo-detail/', todo_detail, name='todo_detail'),
    path('json/', json, name='json'),
    path('from-dart/', from_dart, name='from-dart'),
]