from django.db import models

# Create your models here.
class Event(models.Model):
    eventName = models.CharField(max_length=30)
    eventTime = models.DateField()
    eventDescription = models.TextField()