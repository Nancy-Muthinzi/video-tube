from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Merchant(models.Model):
    first_name = models.CharField(max_length = 25)
    last_name = models.CharField(max_length = 25)
    email = models.EmailField()

class Video(models.Model):
    title = models.CharField(max_length = 50)
    link = models.URLField()
    post = models.TextField()
    merchant = models.ForeignKey(Merchant)
