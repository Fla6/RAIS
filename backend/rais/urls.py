from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.aboutus, name='aboutus'),
    path('', views.home1, name='home1'),
    path('', views.profile, name='profile'),
]

