from django.db import models
from django.shortcuts import get_object_or_404
from django.conf import settings
# Create your models here.
class Event(models.Model):
    Name = models.CharField(max_length=30)
    Time = models.DateField()
    Description = models.TextField()
    #author = models.ForeignKey(settings.AUTH_USER_MODEL,
        #null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.Name
