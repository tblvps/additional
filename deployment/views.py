from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def profile(request):
    return render(request, 'profile.html')

def o(request):
    return render(request, '429.html')

def recover(request):
    return render(request, 'allauth/layouts/recover.html')
