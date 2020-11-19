from django.shortcuts import render
from rais.models import User, Post


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
