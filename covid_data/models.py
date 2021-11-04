from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings
# Create your models here.

class SearchedCovidData(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
        null=True, blank=True, on_delete=models.SET_NULL)
    provinsi = models.CharField(max_length=30)
    kasus_positif = models.CharField(max_length=10)
    kasus_sembuh = models.CharField(max_length=10)
    kasus_meninggal = models.CharField(max_length=10)