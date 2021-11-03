from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class SearchedCovidData(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)
    provinsi = models.CharField(max_length=30)
    kasus_positif = models.CharField(max_length=10)
    kasus_sembuh = models.CharField(max_length=10)
    kasus_meninggal = models.CharField(max_length=10)