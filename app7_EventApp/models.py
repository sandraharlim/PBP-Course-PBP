from django.db import models
# Create your models here.
class Event(models.Model):
    Name = models.CharField(max_length=30)
    Time = models.DateField()
    Description = models.TextField()

    def __str__(self):
        return self.Name
