from django.shortcuts import render, redirect
from .forms import TextFileUploadForm
from .utils import set_env_variable

def success(request):
    return render(request, 'success.html')

def save_env(request):
    if request.method == 'POST':
        key = request.POST.get('key')
        value = request.POST.get('value')
        if key and value:
            set_env_variable(value, key)
            return redirect('success')
    return render(request, 'save_env.html')
