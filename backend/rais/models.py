from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    town = models.CharField(max_length=30)
    birthdate = models.DateField()
    phone = models.CharField(max_length=12)
    email = models.CharField(max_length=100, primary_key=True)
    password = models.CharField(max_length=100)
    token = models.CharField(max_length=500)


class Post(models.Model):
    author = models.ForeignKey('User', on_delete=models.CASCADE)
    text = models.CharField(max_length=10000)
