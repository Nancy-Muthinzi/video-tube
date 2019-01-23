from django.db import models
from django.contrib.auth.models import User
# import datetime as dt

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profile', default=True)
    first_name = models.CharField(max_length = 25)
    last_name = models.CharField(max_length = 25)
    profile_pic = models.ImageField(upload_to='profile/', default=True)
    email = models.EmailField()

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()
    
    def __str__(self):
        return self.first_name + " " + self.last_name

    class Meta:
        ordering = ['first_name', 'last_name']


class Merchant(models.Model):
    first_name = models.CharField(max_length = 25)
    last_name = models.CharField(max_length = 25)
    email = models.EmailField()
    
class Video(models.Model):
    title = models.CharField(max_length = 50)
    link = models.URLField()

    def __str__(self):
        return self.link   

