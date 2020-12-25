from django.db import models
from users.models import Provider


class Listing(models.Model):
    listing_id = models.AutoField(primary_key=True)
    provider = models.ForeignKey(Provider, on_delete = models.CASCADE)
    speciality = models.TextField()
    description = models.TextField()
    ethnicity = models.CharField(max_length=20)
    consultation_charges = models.IntegerField()

    def __str__(self):
        return f'{self.provider} {self.speciality}'
    