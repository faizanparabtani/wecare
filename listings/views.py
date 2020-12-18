from django.shortcuts import render


def home(request):
    # context = {
    #     'posts': Post.objects.all()
    # }
    return render(request, 'listings/home.html')

def dashboard(request):
    # context = {
    #     'posts': Post.objects.all()
    # }
    return render(request, 'listings/dashboard.html')

def providerdashboard(request):
    return render(request, 'listings/provider_dashboard.html')