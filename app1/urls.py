from django.urls import path
from .views import matkul_list, matkul_create, home, json

urlpatterns = [
    path('', home, name='schedule'),
    path('matkul-list/', matkul_list, name='list-matkul'),
    path('create-matkul/', matkul_create, name='create-matkul'),
    path('json/', json, name='json'),
]