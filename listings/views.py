from django.shortcuts import render, get_object_or_404, redirect
from .models import Listing
from itertools import chain
from healthdata.models import HealthData
from django.http import JsonResponse, Http404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
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
from .forms import EditListingForm, AddSeekerForm, RemoveSeekerForm
from healthdata.models import HealthData, Fact

# from django_filters.views import FilterView


def home(request):
    return render(request, 'listings/home.html')


def dashboard(request):
    seeker = get_object_or_404(Seeker, user=request.user)

    fact = Fact.objects.filter(ethnicity=seeker.ethnicity)
    fact = fact[0].fact

    listing_filter = ListingFilter(request.GET, queryset=Listing.objects.all())

    # Pagination
    paginator = Paginator(listing_filter.qs, 4)
    page_number = request.GET.get('page')

    try:
        response = paginator.page(page_number)
    except PageNotAnInteger:
        response = paginator.page(1)
    except EmptyPage:
        response = paginator.page(paginator.num_pages)

    # User HealthData
    user_healthdata = HealthData.objects.filter(seeker=seeker)
    if len(user_healthdata) > 0:
        latest_date = user_healthdata.reverse()[0]
    else:
        latest_date = None

    # Setting Context to send to template
    context = {
        'fact': fact,
        'seeker': seeker,
        'filter': listing_filter,
        'page': page_number,
        'response': response,
        'user_healthdata': user_healthdata,
        'latest_date': latest_date
    }
    return render(request, 'listings/dashboard.html', context)


def providerdashboard(request):
    provider = get_object_or_404(Provider, user=request.user)
    if request.method == 'POST':
        form = AddSeekerForm(request.POST, instance=provider)
        if form.is_valid():
            form.save()
            return redirect('p_dashboard')
        else:
            form = AddSeekerForm()

    is_consulting = IsConsulting.objects.filter(
        provider=provider).values_list('seeker', flat=True)

    if is_consulting != None:
        us = HealthData.objects.filter(seeker__in=is_consulting)
        healthdata_filter = HealthDataFilter(
            request.GET, queryset=us)
    else:
        healthdata_filter = None
        us = None

    # Pagination
    paginator = Paginator(healthdata_filter.qs, 4)
    page_number = request.GET.get('page')

    try:
        response = paginator.page(page_number)
    except PageNotAnInteger:
        response = paginator.page(1)
    except EmptyPage:
        response = paginator.page(paginator.num_pages)

    context = {
        'form': AddSeekerForm,
        'page': page_number,
        'response': response,
        'healthdata_filter': healthdata_filter,
        'us': us,
    }
    return render(request, 'listings/provider_dashboard.html', context)


class AddSeekerView(LoginRequiredMixin, CreateView):
    model = IsConsulting
    fields = ['seeker']
    success_url = '/providerdashboard'

    def form_valid(self, form):
        form.instance.provider = self.request.user.provider
        return super().form_valid(form)


class ListingView(LoginRequiredMixin, DetailView):
    model = Listing

    def get(self, request, pk):
        listing = get_object_or_404(Listing, listing_id=pk)
        provider = listing.provider
        provider = Provider.objects.filter(user=provider)
        provider = provider[0]
        context = {
            'provider': provider,
            'listing': listing
        }

        return render(request, 'listings/listing.html', context)


class SeekerRemoveView(DeleteView):
    success_url = 'providerdashboard'

    def get(self, request, pk, *args, **kwargs):
        provider = request.user.provider
        provider_id = provider.pk
        seeker_id = pk
        is_conulting_obj = IsConsulting.objects.filter(
            seeker=seeker_id, provider=provider_id)
        if is_conulting_obj != None:
            is_conulting_obj.delete()
        return redirect('/providerdashboard')


# class SeekerRemoveView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
#     model = IsConsulting
#     success_url = '/p_dashboard'

#     def test_func(self):
#         return True
        # provider = get_object_or_404(Provider, user=self.request.user)
        # if provider == record.seeker:
        #     return True
        # return False


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
