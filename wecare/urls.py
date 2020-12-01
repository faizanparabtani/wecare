from django.contrib import admin
from django.urls import path
from listings import views as listings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', listings.home),
]
