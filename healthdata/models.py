from django.db import models
from django.utils import timezone
from users.models import Seeker, Provider
from django.core.validators import MaxValueValidator, MinValueValidator


class HealthData(models.Model):
    seeker = models.ForeignKey(Seeker, on_delete=models.CASCADE)
    heartrate = models.IntegerField(
        validators=[MaxValueValidator(210), MinValueValidator(50)])
    weight = models.IntegerField()
    steps = models.IntegerField()
    blood_pressure = models.IntegerField(
        validators=[MaxValueValidator(180), MinValueValidator(60)], null=True, blank=True)
    date_recorded = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.seeker} on {self.date_recorded}'


class Fact(models.Model):
    ethnicity = models.CharField(max_length=30)
    fact = models.TextField(max_length=300)
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.ethnicity}'
