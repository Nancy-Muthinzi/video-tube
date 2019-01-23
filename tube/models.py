from django.db import models
from django.contrib.auth.models import User
import datetime as dt 

# Create your models here.

class Video(models.Model):
    title = models.CharField(max_length = 50)
    link = models.URLField()
    post = models.TextField()
    merchant = models.ForeignKey(User, on_delete=models.CASCADE)
