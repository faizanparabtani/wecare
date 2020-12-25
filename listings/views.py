from django.shortcuts import render
from .models import Listing
from healthdata.models import HealthData
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .filters import ListingFilter, HealthDataFilter
# from django_filters.views import FilterView

def home(request):
    return render(request, 'listings/home.html')

def dashboard(request):
    listing = Listing.objects.all()
    listing_filter = ListingFilter(request.GET, queryset=listing)
    context = {
        'listings': Listing.objects.all(),
        'filter': listing_filter
    }
    return render(request, 'listings/dashboard.html', context)



def providerdashboard(request):
    healthdata = HealthData.objects.all()
    healthdata_filter = HealthDataFilter(request.GET, queryset=healthdata)
    context = {
        'healthdata': HealthData.objects.all(),
        'healthdata_filter': healthdata_filter
    }
    return render(request, 'listings/provider_dashboard.html', context)


class ListingView(LoginRequiredMixin, DetailView):
    model = Listing
    template_name = "listings/listing.html"

# Class Based Dashboard
# class Dashboard(LoginRequiredMixin, ListView, FilterView):
#     model = Listing
#     template_name = 'listings/dashboard.html'

#     context_object_name = 'listings'

#     def search(request):
#         listing = Listing.objects.all()
#         listing_filter = ListingFilter(request.GET, queryset=listing)
#         return {'filter': listing_filter}
    # ordering = ['-date_posted']

    # def get_queryset(self):
    #     prociders = get_object_or_404(Provider, username=self.kwargs.get('username'))
    #     return Post.objects.filter(author=user).order_by('-date_posted')