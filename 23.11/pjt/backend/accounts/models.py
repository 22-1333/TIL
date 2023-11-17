from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(max_length=254, blank=True, null=True)
    registered_products = models.TextField(blank=True, null=True)
    
    USERNAME_FIELD = 'username'