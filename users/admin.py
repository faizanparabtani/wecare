from django.contrib import admin
from .models import User, Seeker, Provider, IsConsulting


admin.site.register(User)
admin.site.register(Seeker)
admin.site.register(Provider)
admin.site.register(IsConsulting)
