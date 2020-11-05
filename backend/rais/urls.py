from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('home1/', views.home1, name='home1'),
    path('profile/', views.profile, name='profile'),
    path('login/', views.login, name='login'),
    path('whats-in-your-mind/', views.whatsinyourmind, name='whats-in-your-mind'),
    path('post/', views.post, name='post'),
    path('edit/', views.post, name='edit'),

]

