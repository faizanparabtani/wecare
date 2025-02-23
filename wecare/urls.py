from listings.models import Listing
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from listings import views as listings
from users import views as users
from listings.filters import ListingFilter
from django_filters.views import FilterView
from healthdata import views as healthdata
from healthdata.views import AddDataView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', listings.home, name='home'),
    path('logout/', auth_views.LogoutView.as_view(template_name='listings/home.html'), name='logout'),
    # path('dashboard', listings.Dashboard.as_view(filterset_class=ListingFilter), name='dashboard'),
    path('dashboard', listings.dashboard, name='dashboard'),
    path('workout_chart/', healthdata.workout_chart, name='workout_chart'),
    path('listing/<int:pk>/', listings.ListingView.as_view(), name='listing'),
    # path('listing<>', listings.listing, name='listing'),
    path('providerdashboard', listings.providerdashboard, name='p_dashboard'),
    # path('track', AddDataView.as_view(), name='track'),
    path('track', healthdata.track, name='track'),
    path('users/', include('users.urls')),
    path('mylisting/', listings.mylisting, name='mylisting'),
    path('delete/<int:pk>', healthdata.RecordDeleteView.as_view(), name='delete'),
    path('add_data/', healthdata.AddDataView.as_view(), name='add_class'),
    path('add_seeker/', listings.AddSeekerView.as_view(), name='add_seeker'),
    path('remove_seeker/<int:pk>',
         listings.SeekerRemoveView.as_view(), name='remove_seeker')
    # path('addseeker<int:pk>/', listings.AddSeekerView.as_view(), name='addseeker')
    # path('profile/', users.provider_setting, name='p_profile')
    # path('mylisting/', listings.MyListing.as_view(), name='mylisting'),
]
