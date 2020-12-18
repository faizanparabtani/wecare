from django.db import models
from users.models import Provider


class Listings(models.Model):
    provider = models.OneToOneField(Provider, on_delete = models.CASCADE, primary_key = True)
    ethnicity = models.CharField(max_length=20)
    consultation_charges = models.IntegerField()
    