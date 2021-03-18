from django.shortcuts import render, get_object_or_404
from .models import Listing
from healthdata.models import HealthData
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .filters import ListingFilter, HealthDataFilter
from users.models import Seeker
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# from django_filters.views import FilterView


def home(request):
    return render(request, 'listings/home.html')


def dashboard(request):
    seeker = get_object_or_404(Seeker, user=request.user)

    listing_filter = ListingFilter(request.GET, queryset=Listing.objects.all())

    # Pagination
    paginator = Paginator(listing_filter.qs, 1)
    page_number = request.GET.get('page')
    # page_obj = paginator.get_page(page_number)

    try:
        response = paginator.page(page_number)
    except PageNotAnInteger:
        response = paginator.page(1)
    except EmptyPage:
        response = paginator.page(paginator.num_pages)

    # Setting Context to send to template
    context = {
        'seeker': seeker,
        'filter': listing_filter,
        'page': page_number,
        'response': response
    }
    return render(request, 'listings/dashboard.html', context)


def workout_chart(request):
    labels = []
    data = []

    seeker = get_object_or_404(Seeker, user=request.user)

    try:
        user_healthdata = HealthData.objects.filter(seeker=seeker)
        for userdata in user_healthdata:
            labels.append(userdata.date_recorded)
            data.append(userdata.steps)
            print(labels, data)
    except:
        user_healthdata = None
        print('Hello')

    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })


def providerdashboard(request):
    healthdata = HealthData.objects.all()
    healthdata_filter = HealthDataFilter(request.GET, queryset=healthdata)
    context = {
        'healthdata': HealthData.objects.all(),
        'healthdata_filter': healthdata_filter
    }
    return render(request, 'listings/provider_dashboard.html', context)


class ListingView(LoginRequiredMixin, DetailView):
    paginate_by = 3
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
