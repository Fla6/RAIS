from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    country = models.CharField(max_length=100, null=True)
    town = models.CharField(max_length=30, null=True)
    birthdate = models.DateField(null=True)
    phone = models.CharField(max_length=12, null=True)
    email = models.CharField(max_length=100)
    password = models.BigIntegerField()
    token = models.CharField(max_length=500)


class Post(models.Model):
    author = models.ForeignKey('User', on_delete=models.CASCADE)
    text = models.CharField(max_length=10000)
