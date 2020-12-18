from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from listings import views as listings
from users import views as users

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', listings.home, name='home'),
    path('logout/', auth_views.LogoutView.as_view(template_name='lisitngs/home.html'), name='logout'),
    path('dashboard', listings.dashboard, name='dashboard'),
    path('providerdashboard', listings.providerdashboard, name='p_dashboard'),
    path('users/', include('users.urls')),
]
