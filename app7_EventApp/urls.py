from django.urls import path
from .views import index, add_event, update_view, DeleteCrudUser

urlpatterns =[
    path("", index, name='EventApp'),
    path('event', add_event, name='event'),
    path('<id>/UpdateEvent', update_view, name="Update"),
    path('ajax/EventApp/delete', DeleteCrudUser.as_view(), name="delete_ajax"),

]