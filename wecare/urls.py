from django.contrib import admin
from django.urls import path, include
from listings import views as listings
from users import views as users
# from providers import views as p_views
# from seekers import views as s_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', listings.home),
    path('users/', include('users.urls')),
    # path('register', p_views.register, name='register'),
    # path('sregister', s_views.register, name='sregister'),
    # path('login', p_views.login, name='login'),
]
