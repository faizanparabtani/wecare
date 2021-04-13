from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from django.views.generic import CreateView
from .forms import SeekerSignUpForm, ProviderSignUpForm, UserUpdateForm, SeekerProfileUpdateForm, ProviderProfileUpdateForm
from django.contrib.auth.forms import AuthenticationForm
from .models import User, Seeker, Provider
from django.views.generic.edit import UpdateView


def register(request):
    return render(request, 'users/register.html')


class seeker_register(CreateView):
    model = User
    form_class = SeekerSignUpForm
    template_name = 'users/seeker_register.html'

    def form_valid(self, form):
        user = form.save()
        messages.success(
            request, f'Your account has been created! You are now able to log in')
        login(self.request, user)
        return redirect('/')


class provider_register(CreateView):
    model = User
    form_class = ProviderSignUpForm
    template_name = 'users/provider_register.html'

    def form_valid(self, form):
        user = form.save()
        messages.success(
            request, f'Your account has been created! You are now able to log in')
        login(self.request, user)
        return redirect('/')


def logindir(request):
    return render(request, 'users/login.html')


def seeker_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            messages.success(request, f'Login Successful')
            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                messages.error(request, "Invalid username or password")
        else:
            messages.error(request, "Invalid username or password")
    return render(request, 'users/seeker_login.html', context={'form': AuthenticationForm()})


def provider_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('p_dashboard')
            else:
                messages.error(request, "Invalid username or password")
        else:
            messages.error(request, "Invalid username or password")
    return render(request, 'users/provider_login.html', context={'form': AuthenticationForm()})


class SeekerProfile(UpdateView):
    model = Seeker
    fields = ['phone_number', 'medicaid_recepient', 'location']
    template_name_suffix = '_update_form'


class ProviderProfile(UpdateView):
    model = Provider
    fields = ['phone_number', 'designation']
    template_name_suffix = '_update_form'


def logout_view(request):
    logout(request)
    return redirect('/')


# Class/function views tried
# def seeker_setting(request):
#     user = request.user
#     user_deets = get_object_or_404(Seeker, user=request.user)

#     if request.method == 'POST':
#         form = UserUpdateForm(request.POST, instance=request.user)
#         s_form = SeekerProfileUpdateForm(
#             request.POST, instance=request.user.seeker)
#         if form.is_valid() and s_form.is_valid():
#             form.save()
#             s_form.save()
#             return redirect('dashboard')

#     context = {
#         'form': UserUpdateForm,
#         's_form': SeekerProfileUpdateForm,
#         'user_deets': user_deets
#     }
#     return render(request, 'users/seeker_setting.html', context)
# def provider_setting(request):
#     user = request.user
#     user_deets = get_object_or_404(Provider, user=request.user)

#     if request.method == 'POST':
#         form = UserUpdateForm(request.POST, instance=request.user)
#         p_form = SeekerProfileUpdateForm(
#             request.POST, instance=request.user.provider)
#         if form.is_valid() and p_form.is_valid():
#             form.save()
#             p_provider.save()
#             return redirect('dashboard')

#     context = {
#         'form': UserUpdateForm,
#         'p_form': ProviderProfileUpdateForm,
#         'user_deets': user_deets
#     }
#     return render(request, 'users/provider_setting.html', context)
