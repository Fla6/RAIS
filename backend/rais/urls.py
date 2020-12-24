from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='home'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('home1/', views.home1, name='home1'),
    path('profile/', views.profile, name='profile'),
    path('login/', views.login, name='login'),
    path('whats-in-your-mind/', views.whatsinyourmind, name='whats-in-your-mind'),
    path('post/', views.post, name='post'),
    path('editpost/', views.edit_post, name='edit_post'),
    path('deletepost/', views.delete_post, name='delete_post'),
    path('home_logout/', views.home_logout, name='home_logout'),
    path('search/', views.search, name='search'),
    path('editprofile/', views.editprofile, name='editprofile'),
]

