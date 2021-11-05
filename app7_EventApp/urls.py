from django.urls import path
from .views import index, add_event, manage_view, update_view, delete_view

urlpatterns =[
    path("", index, name='EventApp'),
    path('event', add_event, name='event'),
    path('ManageEvent', manage_view, name='Manage'),
    path('<id>/UpdateEvent', update_view, name="Update"),
    path('<id>/DeleteEvent', delete_view, name="Delete"),
]