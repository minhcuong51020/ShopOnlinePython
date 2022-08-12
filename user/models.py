from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    phone = models.CharField(max_length=255, default='')
    gender = models.CharField(max_length=255, default='Nam')


class Address(models.Model):
    numberHouse = models.CharField(max_length = 255, default='')
    street = models.CharField(max_length=255, default='')
    distric = models.CharField(max_length=255, default='')
    city = models.CharField(max_length=255, default='')
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)

