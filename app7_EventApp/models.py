from django.db import models
from django.shortcuts import get_object_or_404
# Create your models here.
class Event(models.Model):
    Name = models.CharField(max_length=30)
    Time = models.DateField()
    Description = models.TextField()


    def __str__(self):
        return self.Name
