from django.db import models

# Create your models here.
class InfoPandemi(models.Model):
    nama = models.CharField(max_length=100)
    pekerjaan = models.CharField(max_length=100)
    konten = models.TextField()

class TipsKesehatan(models.Model):
    nama = models.CharField(max_length=100)
    pekerjaan = models.CharField(max_length=100)
    konten = models.TextField()

class CurahanHati(models.Model):
    nama = models.CharField(max_length=100)
    pekerjaan = models.CharField(max_length=100)
    konten = models.TextField()