from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.


@csrf_exempt
def index(request):
    print('index')
    return render(request=request, template_name='rais/home.html')


def aboutus(request):
    print('aboutus')
    return render(request=request, template_name='rais/aboutus.html')


def home1(request):
    return render(request=request, template_name='rais/home1.html')


def profile(request):
    return render(request=request, template_name='rais/profile.html')


@csrf_exempt
def login(request):
    return render(request=request, template_name='rais/login.html')


def whatsinyourmind(request):
    return render(request=request, template_name='rais/whats-in-your-mind.html')

def post(request):
    return render(request=request, template_name='rais/post.html')
