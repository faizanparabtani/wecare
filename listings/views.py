from django.shortcuts import render, get_object_or_404, redirect
from .models import Listing
from healthdata.models import HealthData
from django.http import JsonResponse, Http404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from rest_framework.response import Response
from rest_framework import status
from urllib.error import HTTPError
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    FormView
)
from .filters import ListingFilter, HealthDataFilter
from users.models import User, Seeker, Provider, IsConsulting
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import EditListingForm, AddSeekerForm

# from django_filters.views import FilterView


def home(request):
    return render(request, 'listings/home.html')


def dashboard(request):
    labels = []
    data = []
    seeker = get_object_or_404(Seeker, user=request.user)

    listing_filter = ListingFilter(request.GET, queryset=Listing.objects.all())

    # Pagination
    paginator = Paginator(listing_filter.qs, 4)
    page_number = request.GET.get('page')
    # page_obj = paginator.get_page(page_number)

    try:
        response = paginator.page(page_number)
    except PageNotAnInteger:
        response = paginator.page(1)
    except EmptyPage:
        response = paginator.page(paginator.num_pages)

    # User HealthData
    user_healthdata = HealthData.objects.filter(seeker=seeker)
    latest_date = user_healthdata.reverse()[0]

    # Setting Context to send to template
    context = {
        'seeker': seeker,
        'filter': listing_filter,
        'page': page_number,
        'response': response,
        'user_healthdata': user_healthdata,
        'latest_date': latest_date
    }
    return render(request, 'listings/dashboard.html', context)


def providerdashboard(request):
    user_lis = []
    if request.method == 'POST':
        form = AddSeekerForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('p_dashboard')
        else:
            form = AddSeekerForm(instance=request.user)

    # user = User.objects.filter(provider=request.user)
    provider = get_object_or_404(Provider, user=request.user)
    is_consulting = IsConsulting.objects.filter(provider=provider)
    if is_consulting != None:
        for i in is_consulting:
            try us = get_object_or_404(HealthData, user=i.seeker):
                user_lis.append(us)
            except HTTPError:
                pass

    healthdata = HealthData.objects.all()
    healthdata_filter = HealthDataFilter(request.GET, queryset=healthdata)
    context = {
        'form': AddSeekerForm,
        'healthdata': HealthData.objects.all(),
        'healthdata_filter': healthdata_filter
    }
    return render(request, 'listings/provider_dashboard.html', context)


class ListingView(LoginRequiredMixin, DetailView):
    model = Listing

    def get(self, request, pk):
        listing = get_object_or_404(Listing, listing_id=pk)
        provider = listing.provider
        provider = Provider.objects.filter(user=provider)
        provider = provider
        context = {
            'provider': provider,
            'listing': listing
        }

        return render(request, 'listings/listing.html', context)


class MyListing(LoginRequiredMixin, UpdateView):
    model = Listing
    form_class = EditListingForm
    template_name = 'listings/mylisting.html'
    success_url = 'p_dashboard'

    def form_valid(self, form):
        return super().form_valid(form)

    def get(self, request):
        provider = get_object_or_404(Provider, user=request.user)
        listings = Listing.objects.filter(provider=provider)
        context = {
            'listings': listings,
            'provider': provider,
        }
        return render(request, 'listings/mylisting.html', context)


def mylisting(request):
    provider = get_object_or_404(Provider, user=request.user)
    try:
        listing = get_object_or_404(Listing, provider=provider)
    except Http404:
        listing = None
    if request.method == 'POST':
        form = EditListingForm(request.POST, instance=listing)
        if form.is_valid():
            form.save()
            return redirect('mylisting')
    else:
        form = EditListingForm(instance=listing)

    context = {
        'form': EditListingForm,
        'listing': listing
    }
    return render(request, 'listings/mylisting.html', context)

# class EditListing(LoginRequiredMixin, DetailView):
#     model = Listing

#     def(self, request, pk):
#         listing = Listing

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
