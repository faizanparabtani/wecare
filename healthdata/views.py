from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import DeleteView
from .forms import AddHealthData
from django.http import JsonResponse, Http404
from django.views.generic import CreateView
from .models import HealthData
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from users.models import Seeker
from .forms import AddHealthData
import logging


def track(request):
    seeker = get_object_or_404(Seeker, user=request.user)
    healthdata = HealthData.objects.filter(seeker=seeker)
    latest_date = healthdata.reverse()[0]
    if request.method == 'POST':
        form = AddHealthData(request.POST, instance=seeker)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = AddHealthData(instance=seeker)

    context = {
        'form': AddHealthData,
        'seeker': seeker,
        'healthdata': healthdata,
        'latest_date': latest_date
    }

    return render(request, 'healthdata/track.html', context)


logger = logging.getLogger(__name__)


class AddDataView(LoginRequiredMixin, CreateView):
    model = HealthData
    fields = ['heartrate', 'steps', 'weight', 'blood_pressure']
    template_name = 'healthdata/track.html'
    success_url = '/dashboard'

    def form_valid(self, form):
        form.instance.seeker = self.request.user.seeker
        return super().form_valid(form)


def workout_chart(request):
    labels = []
    data = []

    seeker = get_object_or_404(Seeker, user=request.user)

    try:
        user_healthdata = HealthData.objects.filter(seeker=seeker)
        for userdata in user_healthdata:
            date_recorded = userdata.date_recorded.strftime('%m/%d')
            labels.append(date_recorded)
            data.append(userdata.steps)
    except:
        user_healthdata = None

    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })


class RecordDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = HealthData
    success_url = '/track'

    def test_func(self):
        record = self.get_object()
        seeker = get_object_or_404(Seeker, user=self.request.user)
        if seeker == record.seeker:
            return True
        return False

    # return '{}#education'.format(reverse('profile', kwargs={'pk': pk}))
# def track(request):
#     print(request.user.seeker)
#     if request.method == "POST":
#         healthform = AddHealthData(instance=request.user.seeker)

#         if healthform.is_valid():
#             healthform.save()
#             return redirect('dashboard')

#     else:
#         healthform = AddHealthData(instance=request.user.seeker)

#     context = {
#         'healthform': healthform
#     }

#     return render(request, 'healthdata/track.html', context)
