from django.urls import path
from .views import add_matkul, matkul_list, json, edit_matkul, delete_matkul

urlpatterns = [
    # path('', index, name='index'),
    path('', add_matkul, name='add-matkul'),
    path('matkul-list', matkul_list, name='list-matkul'),
    path('delete-matkul', delete_matkul, name='delete-matkul'),
    path('edit-matkul', edit_matkul, name='edit-matkul'),
    path('json', json),
]