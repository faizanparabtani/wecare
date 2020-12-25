import django_filters
from .models import Listing
from healthdata.models import HealthData


class ListingFilter(django_filters.FilterSet):
    class Meta:
        model = Listing
        fields = ['provider', 'speciality' ]

class HealthDataFilter(django_filters.FilterSet):
    class Meta:
        model = HealthData
        fields = ['seeker', 'date_recorded' ]