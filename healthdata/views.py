from django.shortcuts import render

def track(request):
    return render(request, 'healthdata/track.html')
