from django.db import models

# Create your models here.
class Post(models.Model):
    post=models.CharField(max_length=100)
    caption=models.CharField(max_length=100)

class History(models.Model):
    post=models.CharField(max_length=100)
    caption=models.CharField(max_length=100)