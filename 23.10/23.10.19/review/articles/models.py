from django.db import models

# Create your models here.
class Topic(models.Model):
    name = models.CharField(max_length=100)


class Article(models.Model):
    topic = models.ManyToManyField(Topic, blank=True, null=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    views = models.IntegerField(default=0)


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
