from django.db import models
from django.conf import settings


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=200)
    price = models.IntegerField()
    description = models.TextField()
    image = models.URLField()
    users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='cart', blank=True)
