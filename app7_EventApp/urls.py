from django.urls import path
from .views import index, add_event

urlpatterns =[
    path('', index, name='EventApp'),
    path('event', add_event, name='event'),
]