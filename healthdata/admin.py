from django.contrib import admin
from .models import HealthData, Fact

admin.site.register(HealthData)
admin.site.register(Fact)
