from django.shortcuts import render
from rais.models import User, Post
import datetime


class HomePage:
    _logout_path = 'rais/home_logout.html'
    _login_path = 'rais/home_login.html'

    def __init__(self, request):
        self._request = request

    def get_login_page(self):
        posts = reversed(Post.objects.all())
        return render(request=self._request, context={'posts': posts}, template_name=self._login_path)

    def get_logout_page(self):
        posts = reversed(Post.objects.all())
        return render(request=self._request, context={'posts': posts}, template_name=self._logout_path)


class PostPage:
    _path = 'rais/post.html'

    def __init__(self, request):
        self._request = request

    def get_page(self):
        return render(request=self._request, template_name=self._path)


class EditProfilePage:
    _path = 'rais/editprofile.html'

    def __init__(self, request):
        self._request = request

    def get_page(self):
        user = User.objects.get(token=self._request.COOKIES['token'])
        context = {
            'name': user.name,
            'surname': user.surname,
            'username': user.username,
            'birthdate': datetime.datetime.strftime(user.birthdate, '%Y-%m-%d'),
            'town': user.town,
            'country': user.country,
            'phone': user.phone,
            'email': user.email
        }

        return render(request=self._request, context=context, template_name=self._path)


class AboutUsPage:
    _logout_path = 'rais/aboutus_logout.html'
    _login_path = 'rais/aboutus_login.html'

    def __init__(self, request):
        self._request = request

    def get_login_page(self):
        return render(request=self._request, template_name=self._login_path)

    def get_logout_page(self):
        return render(request=self._request, template_name=self._logout_path)


class SearchResultsPage:
    _logout_path = 'rais/home_logout.html'
    _login_path = 'rais/home_login.html'

    def __init__(self, request):
        self._request = request

    def get_login_page(self):
        posts = reversed(Post.objects.all())
        sorted_posts = []
        for post in posts:
            if self._request.POST['request'] in post.text:
                sorted_posts.append(post)
        return render(request=self._request, context={'posts': sorted_posts}, template_name=self._login_path)

    def get_logout_page(self):
        posts = reversed(Post.objects.all())
        sorted_posts = []
        for post in posts:
            if self._request['request'] in post.text:
                sorted_posts.append(post)
        return render(request=self._request, context={'posts': sorted_posts}, template_name=self._logout_path)


class ProfilePage:
    _path = 'rais/profile_login.html'

    def __init__(self, request):
        self._request = request

    def get_page(self):
        user = User.objects.get(token=self._request.COOKIES['token'])
        posts = reversed(Post.objects.filter(author=user))
        context = {
            'name': user.name + ' ' + user.surname,
            'username': user.username,
            'birthdate': user.birthdate,
            'town': user.town,
            'country': user.country,
            'phone': user.phone,
            'email': user.email,
            'posts': posts
        }
        return render(request=self._request, context=context, template_name=self._path)
