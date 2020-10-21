from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request=request, template_name='rais/home.html')

def aboutus(request):
    return render(request=request, template_name='rais/aboutus.html')

def home1(request):
    return render(request=request, template_name='rais/home1.html')

def profile(request):
    return render(request=request, template_name='rais/profile.html')
