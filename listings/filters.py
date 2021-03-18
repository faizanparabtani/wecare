import django_filters
from .models import Listing
from healthdata.models import HealthData
from users.models import Provider


class ListingFilter(django_filters.FilterSet):
    speciality = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Listing
        fields = ['speciality']


class HealthDataFilter(django_filters.FilterSet):
    class Meta:
        model = HealthData
        fields = ['seeker', 'date_recorded']
