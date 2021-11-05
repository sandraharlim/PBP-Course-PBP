from django.urls import path
from .views import todo_index, todo_detail, todo_delete

urlpatterns = [
    path('', todo_index, name='index'),
    path('todo-delete/', todo_delete, name='todo_delete'),
    path('<id>/todo-detail/', todo_detail, name='todo_detail'),
]