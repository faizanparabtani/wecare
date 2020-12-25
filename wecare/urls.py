from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from listings import views as listings
from users import views as users
from listings.filters import ListingFilter
from django_filters.views import FilterView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', listings.home, name='home'),
    path('logout/', auth_views.LogoutView.as_view(template_name='listings/home.html'), name='logout'),
    # path('dashboard', listings.Dashboard.as_view(filterset_class=ListingFilter), name='dashboard'),
    path('dashboard', listings.dashboard, name='dashboard'),
    path('listing/<int:pk>/', listings.ListingView.as_view(), name='listing'),
    # path('listing<>', listings.listing, name='listing'),
    path('providerdashboard', listings.providerdashboard, name='p_dashboard'),
    path('users/', include('users.urls')),
]
