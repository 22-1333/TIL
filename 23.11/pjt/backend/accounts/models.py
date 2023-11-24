from django.db import models
from django.contrib.auth.models import AbstractUser
from interests.models import Product

# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=30, unique=True)
    nickname = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(max_length=254, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    money = models.IntegerField(blank=True, null=True)
    salary = models.IntegerField(blank=True, null=True)

    registered_products = models.ManyToManyField(Product, related_name='registering_users')

    duration = models.IntegerField(blank=True, null=True)