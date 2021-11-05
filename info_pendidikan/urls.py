from django.urls import path
from .views import info_pendidikan

urlpatterns = [
    path('', info_pendidikan, name='info_pendidikan'),
    # path('', search_news, name='search_news'),
]
