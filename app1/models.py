from django.db import models
from django.conf import settings

class Matkul(models.Model):

    name = models.CharField(max_length=255)
    day = models.CharField(max_length=255)
    start_time = models.TimeField()
    end_time = models.TimeField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name