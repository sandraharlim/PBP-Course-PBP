from django.urls import path
from .views import covid_data, search, searchF, getModelsF

urlpatterns = [
    path('', covid_data, name='covid_data'),
    path('data/', search, name='search'),
    path('data/json', searchF, name='searchF'),
    path('getmodels', getModelsF, name='getModelsF'),
]