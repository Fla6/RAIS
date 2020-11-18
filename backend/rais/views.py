from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from rais.models import User, Post
import datetime
import os
import base64


# Create your views here.


@csrf_exempt
def index(request):
    if 'token' in request.COOKIES:

        if len(request.COOKIES['token']) != 0:
            user = None
            try:
                user = User.objects.get(token=request.COOKIES['token'])
            except User.DoesNotExist:
                return render(request=request, template_name='rais/home_logout.html')
            else:
                return render(request=request, template_name='rais/home_login.html')

        else:
            return render(request=request, template_name='rais/home_logout.html')

    else:
        return render(request=request, template_name='rais/home_logout.html')


def home_logout(request):
    response = render(request=request, template_name='rais/home_logout.html')
    response.set_cookie('token', '')
    return response


def aboutus(request):
    if 'token' in request.COOKIES:

        if len(request.COOKIES['token']) != 0:
            user = None
            try:
                user = User.objects.get(token=request.COOKIES['token'])
            except User.DoesNotExist:
                return render(request=request, template_name='rais/aboutus_logout.html')
            else:
                return render(request=request, template_name='rais/aboutus_login.html')

        else:
            return render(request=request, template_name='rais/aboutus_logout.html')

    else:
        return render(request=request, template_name='rais/aboutus_logout.html')


def home1(request):
    return render(request=request, template_name='rais/home1.html')


def profile(request):
    if 'token' in request.COOKIES:

        if len(request.COOKIES['token']) != 0:
            user = None
            try:
                user = User.objects.get(token=request.COOKIES['token'])
            except User.DoesNotExist:
                return render(request=request, template_name='rais/home_logout.html')
            else:
                context = {
                    'name': user.name + ' ' + user.surname,
                    'birthdate': user.birthdate,
                    'town': user.town,
                    'country': user.country,
                    'phone': user.phone,
                    'email': user.email
                }

                return render(request=request, context=context, template_name='rais/profile_login.html')

        else:
            return render(request=request, template_name='rais/home_logout.html')

    else:
        return render(request=request, template_name='rais/home_logout.html')


@csrf_exempt
def login(request):
    # Если регистрируется новый пользователь
    if len(request.POST) == 10:

        # Генерируем уникальный токен пользователя
        token = base64.b64encode(os.urandom(256)).decode('utf-8')

        user = User(name=request.POST['name'],
                    surname=request.POST['surname'],
                    username=request.POST['username'],
                    country=request.POST['country'],
                    town=request.POST['town'],
                    birthdate=datetime.datetime.strptime(request.POST['birthdate'], '%Y-%m-%d').date(),
                    phone=request.POST['phone'],
                    email=request.POST['email'],
                    password=request.POST['password'],
                    token=token
                    )
        user.save()

        response = render(request=request, template_name='rais/home_login.html')
        # Устанавливаем куку с токеном в браузере пользователя
        response.set_cookie('token',
                            value=token,
                            expires=datetime.datetime.utcnow() + datetime.timedelta(days=30))

        return response

    # Если зарегистрированный пользователь осуществляет вход
    elif len(request.POST) in [2, 3]:
        user = None
        try:
            user = User.objects.get(email=request.POST['email'])
        # Если пользователя с такой почтой не существует
        except User.DoesNotExist:
            return render(request=request, template_name='rais/home_logout.html')
        else:
            # Если пароль введён верно
            if user.password == request.POST['password']:
                response = render(request=request, template_name='rais/home_login.html')

                if 'remember' in request.POST:
                    if request.POST['remember'] == 'on':
                        response.set_cookie('token',
                                            value=user.token,
                                            expires=datetime.datetime.utcnow() + datetime.timedelta(days=30))
                    else:
                        response.set_cookie('token', value=user.token)
                else:
                    response.set_cookie('token', value=user.token)

                return response
            else:
                return render(request=request, template_name='rais/home_logout.html')
    else:
        return render(request=request, template_name='rais/home_logout.html')

def whatsinyourmind(request):
    if 'token' in request.COOKIES:

        if len(request.COOKIES['token']) != 0:
            user = None
            try:
                user = User.objects.get(token=request.COOKIES['token'])
            except User.DoesNotExist:
                return render(request=request, template_name='rais/login.html')
            else:
                return render(request=request, template_name='rais/whats-in-your-mind-login.html')

        else:
            return render(request=request, template_name='rais/login.html')

    else:
        return render(request=request, template_name='rais/whats-in-your-mind-logout.html')


def post(request):
    if 'token' in request.COOKIES:

        if len(request.COOKIES['token']) != 0:
            user = None
            try:
                user = User.objects.get(token=request.COOKIES['token'])
            except User.DoesNotExist:
                return render(request=request, template_name='rais/home_logout.html')
            else:
                if 'editor1' in request.GET:
                    if len(request.GET['editor1']) > 0:
                        new_post = Post()
                        new_post.author = user
                        new_post.text = request.GET['editor1']
                        new_post.save()
                        return render(request=request, template_name='rais/post.html')
                    else:
                        return render(request=request, template_name='rais/post.html')
                else:
                    return render(request=request, template_name='rais/post.html')
        else:
            return render(request=request, template_name='rais/home_logout.html')
    else:
        return render(request=request, template_name='rais/home_logout.html')


def edit(request):
    return render(request=request, template_name='rais/edit.html')
