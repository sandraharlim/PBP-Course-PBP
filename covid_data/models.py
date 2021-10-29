from django.db import models

# Create your models here.
class SearchedCovidData(models.Model):
    user = models.ForeignKey
    provinsi = models.CharField(max_length=30)
    kasus_positif = models.CharField(max_length=10)
    kasus_sembuh = models.CharField(max_length=10)
    kasus_meninggal = models.CharField(max_length=10)