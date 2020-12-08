from django.urls import path
from .import  views

urlpatterns=[
     path('register/',views.register, name='register'),
     path('seeker_register/',views.seeker_register.as_view(), name='seeker_register'),
     path('provider_register/',views.provider_register.as_view(), name='provider_register'),
     path('login/',views.login_request, name='login'),
     path('logout/',views.logout_view, name='logout'),
]