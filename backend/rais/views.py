from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from rais.models import User
import datetime


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
    # Если регистрируется новый пользователь
    if len(request.POST) == 10:
        user = User(name=request.POST['name'],
                    surname=request.POST['surname'],
                    username=request.POST['username'],
                    country=request.POST['country'],
                    town=request.POST['town'],
                    birthdate=datetime.datetime.strptime(request.POST['birthdate'], '%Y-%m-%d').date(),
                    phone=request.POST['phone'],
                    email=request.POST['email'],
                    password=request.POST['password']
                    )
        user.save()
        return render(request=request, template_name='rais/login.html')

    # Если зарегистрированный пользователь осуществляет вход
    elif len(request.POST) == 2:
        user = None
        try:
            user = User.objects.get(email=request.POST['email'])
        # Если пользователя с такой почтой не существует
        except User.DoesNotExist:
            return render(request=request, template_name='rais/home.html')
        else:
            # Если пароль введён верно
            if user.password == request.POST['password']:
                return render(request=request, template_name='rais/login.html')
            else:
                return render(request=request, template_name='rais/home.html')
    else:
        return render(request=request, template_name='rais/home.html')

def whatsinyourmind(request):
    return render(request=request, template_name='rais/whats-in-your-mind.html')


def post(request):
    return render(request=request, template_name='rais/post.html')


def edit(request):
    return render(request=request, template_name='rais/edit.html')
