from django.urls import path
from .views import add_info_pandemi, add_tips_kesehatan, add_curahan_hati, button, search_info_pandemi, search_curahan_hati, search_tips_kesehatan, get_data, add_data_curahan_hati, add_data_info_pandemi, add_data_tips_kesehatan

urlpatterns = [
    path('', button, name='button'),
    path('button', button, name='button'),
    path('add_info_pandemi', add_info_pandemi, name='add_info_pandemi'),
    path('add_tips_kesehatan', add_tips_kesehatan, name='add_tips_kesehatan'),
    path('add_curahan_hati', add_curahan_hati, name='add_curahan_hati'),
    path('search_info_pandemi', search_info_pandemi, name='search_info_pandemi'),
    path('search_tips_kesehatan', search_tips_kesehatan, name='search_tips_kesehatan'),
    path('search_curahan_hati', search_curahan_hati, name='search_curahan_hati'),
    path('get_data', get_data, name='get_data'),
    path('add_data_info_pandemi', add_data_info_pandemi, name='add_data_info_pandemi'),
    path('add_data_curahan_hati', add_data_curahan_hati, name='add_data_curahan_hati'),
    path('add_data_tips_kesehatan', add_data_tips_kesehatan, name='add_data_tips_kesehatan'),
]