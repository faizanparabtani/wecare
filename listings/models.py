from django.db import models
from users.models import Provider
from django.shortcuts import reverse


class Listing(models.Model):
    listing_id = models.AutoField(primary_key=True)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    description = models.TextField()
    consultation_charges = models.IntegerField()
    ethnicity = models.CharField(max_length=20)
    speciality = models.TextField()

    def __str__(self):
        return f'{self.provider}'

    def get_absolute_url(self):
        return reverse('mylisting')
        # return reverse('mylisting', kwargs={'pk': self.pk})
