from django.urls import path
from .import  views

urlpatterns=[
     path('register/',views.register, name='register'),
     path('seeker_register/',views.seeker_register.as_view(), name='s_register'),
     path('provider_register/',views.provider_register.as_view(), name='p_register'),
     path('login/',views.logindir, name='login'),
     path('provider_login/',views.provider_login, name='p_login'),
     path('seeker_login/',views.seeker_login, name='s_login'),
     path('seeker_setting/',views.seeker_setting, name='s_setting'),
     path('logout/',views.logout_view, name='logout'),
]