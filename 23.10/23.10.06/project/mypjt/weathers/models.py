from django.db import models

# Create your models here.
class Reply(models.Model):
    problem_num = models.IntegerField(null=True)
    content = models.TextField()