from django.urls import path
from .views import info_pendidikan
# from .views import covid_data, search

urlpatterns = [
    path('', info_pendidikan, name='info_pendidikan'),
    # path('', search_news, name='search_news'),
]
