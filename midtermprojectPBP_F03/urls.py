"""midtermprojectPBP_F03 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from os import stat
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('to-do-list/', include('to_do_list.urls')),
    path('info-pendidikan/', include('info_pendidikan.urls')),
    path('EventApp/', include('app7_EventApp.urls')),
    path('covid-data/', include('covid_data.urls')),
    path('add-forum/', include('forum.urls')),
    path('susun-jadwal-matkul/', include('app1.urls')),
    path('quiz-of-pandemic/', include('quizes.urls'))
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)