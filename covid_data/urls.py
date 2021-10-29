from django.urls import path
from .views import covid_data, search

urlpatterns = [
    path('', covid_data, name='covid_data'),
    path('data/', search, name='search'),
]