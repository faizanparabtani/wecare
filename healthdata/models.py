from django.db import models
from django.utils import timezone
from users.models import Seeker, Provider

class HealthData(models.Model):
    seeker = models.ForeignKey(Seeker, on_delete = models.CASCADE)
    heartrate = models.IntegerField()
    weight = models.IntegerField()
    steps = models.IntegerField()
    date_recorded = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.seeker} on {self.date_recorded}'


# class Consulting(models.Model):
    