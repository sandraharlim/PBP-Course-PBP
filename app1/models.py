from django.db import models
from django.db.models.enums import Choices
# from django.urls import reverse
# from datetime import datetime
# from accounts.models import User

class Matkul(models.Model):
    class Day(models.TextChoices):
        MON = "1", "Monday"
        TUE = "2", "Tuesday"
        WED = "3", "Wednesday"
        THUR = "4", "Thursday"
        FRI = "5", "Friday"

    name = models.CharField(max_length=255)
    day = models.CharField(max_length=255, choices=Day.choices, default=Day.MON)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return self.name