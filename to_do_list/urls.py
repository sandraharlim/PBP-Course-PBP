from django.urls import path
from .views import item_detail, item_list

urlpatterns = [
    path('', item_list, name='item_list'),
    path('item_detail/<str:pk>', item_detail, name='item_detail'),
]