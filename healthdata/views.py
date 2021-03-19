from django.shortcuts import render, redirect
from .forms import AddHealthData
from django.views.generic import CreateView
from .models import HealthData
from django.contrib.auth.mixins import LoginRequiredMixin


class AddDataView(LoginRequiredMixin, CreateView):
    template_name = 'healthdata/track.html'
    success_url = '/dashboard'
    model = HealthData
    fields = ['heartrate', 'steps', 'weight']

    def form_valid(self, form):
        form.instance.seeker = self.request.user.seeker
        return super().form_valid(form)

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
