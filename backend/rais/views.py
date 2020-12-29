from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from rais.models import User, Post
from rais.pages import HomePage, PostPage, AboutUsPage, SearchResultsPage, ProfilePage, EditProfilePage
from rais.authentification import authenticate_user_token, authenticate_user_password
import datetime
import os
import base64
import hashlib


# Create your views here.


@csrf_exempt
def index(request):
    homepage = HomePage(request)
    if authenticate_user_token(request):
        return homepage.get_login_page()
    else:
        return homepage.get_logout_page()


def home_logout(request):
    homepage = HomePage(request)
    response = homepage.get_logout_page()
    response.set_cookie('token', '')
    return response


def aboutus(request):
    about_us_page = AboutUsPage(request)
    if authenticate_user_token(request):
        return about_us_page.get_login_page()
    else:
        return about_us_page.get_logout_page()


def home1(request):
    return render(request=request, template_name='rais/home1.html')


def profile(request):
    homepage = HomePage(request)
    profile_page = ProfilePage(request)

    if authenticate_user_token(request):
        return profile_page.get_page()
    else:
        return homepage.get_logout_page()



@csrf_exempt
def login(request):
    homepage = HomePage(request)

    # Если регистрируется новый пользователь
    if len(request.POST) == 10:

        # Генерируем уникальный токен пользователя
        token = base64.b64encode(os.urandom(256)).decode('utf-8')

        birthdate = None
        if request.POST['birthdate'] != '':
            birthdate = datetime.datetime.strptime(request.POST['birthdate'], '%Y-%m-%d').date()
        
        user = User(name=request.POST['name'],
                    surname=request.POST['surname'],
                    username=request.POST['username'],
                    country=request.POST['country'],
                    town=request.POST['town'],
                    birthdate=birthdate,
                    phone=request.POST['phone'],
                    email=request.POST['email'],
                    password=hashlib.sha256(request.POST['password'].encode('utf-8')).digest(),
                    token=token
                    )
        user.save()

        response = homepage.get_login_page()
        # Устанавливаем куку с токеном в браузере пользователя
        response.set_cookie('token',
                            value=token,
                            expires=datetime.datetime.utcnow() + datetime.timedelta(days=30))

        return response

    # Если зарегистрированный пользователь осуществляет вход
    elif len(request.POST) in [2, 3]:
        if authenticate_user_password(request):
            response = homepage.get_login_page()
            user = User.objects.get(email=request.POST['email'])

            if 'remember' in request.POST and request.POST['remember'] == 'on':
                response.set_cookie('token',
                                    value=user.token,
                                    expires=datetime.datetime.utcnow() + datetime.timedelta(days=30))
            else:
                response.set_cookie('token', value=user.token)
            return response

        # Если пользователь не прошёл аутентификацию
        else:
            return homepage.get_logout_page()

    # Если поступил неизвестный запрос
    else:
        return homepage.get_logout_page()


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


@csrf_exempt
def post(request):
    homepage = HomePage(request)
    postpage = PostPage(request)

    if authenticate_user_token(request):
        if 'editor1' in request.POST and len(request.POST['editor1']) > 0:
            user = User.objects.get(token=request.COOKIES['token'])

            new_post = Post()
            new_post.author = user
            new_post.text = request.POST['editor1']
            new_post.publication_date = datetime.datetime.now()
            new_post.save()

        return postpage.get_page()

    # Если пользователь не прошёл аутентификацию
    else:
        return homepage.get_logout_page()


@csrf_exempt
def edit_post(request):
    return render(request=request, template_name='rais/post.html')


@csrf_exempt
def delete_post(request):
    homepage = HomePage(request)
    profile_page = ProfilePage(request)

    Post.objects.filter(id=int(request.POST['post_id'])).delete()

    if authenticate_user_token(request):
        return profile_page.get_page()
    else:
        return homepage.get_logout_page()


@csrf_exempt
def search(request):
    results_page = SearchResultsPage(request)
    if authenticate_user_token(request):
        return results_page.get_login_page()
    else:
        return results_page.get_logout_page()


@csrf_exempt
def editprofile(request):
    profile_page = ProfilePage(request)
    edit_profile_page = EditProfilePage(request)
    homepage = HomePage(request)

    if request.method == 'GET':
        if authenticate_user_token(request):
            return edit_profile_page.get_page()
        else:
            return homepage.get_logout_page()

    elif request.method == 'POST':
        if authenticate_user_token(request):

            user = User.objects.get(token=request.COOKIES['token'])

            user.name = request.POST['name']
            user.surname = request.POST['surname']
            user.username = request.POST['username']
            user.birthdate = datetime.datetime.strptime(request.POST['birthdate'], '%Y-%m-%d').date()
            user.town = request.POST['town']
            user.country = request.POST['country']
            user.phone = request.POST['phone']
            user.email = request.POST['email']

            user.save()

            return profile_page.get_page()

        else:
            return homepage.get_logout_page()






