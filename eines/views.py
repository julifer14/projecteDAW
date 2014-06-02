from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def error500(request):
    return render(request, '500.html')
