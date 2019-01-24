from django.db import models
from django.contrib.auth.models import User
import datetime as dt 

# Create your models here.
class Video(models.Model):
    title = models.CharField(max_length = 50)            
    link = models.URLField()
    description = models.TextField()
    merchant = models.ForeignKey(User, on_delete=models.CASCADE)

    def save_video(self):
        self.save

    def delete_video(self):
        self.delete

    @classmethod
    def get_all_videos(cls):
        videos = cls.objects.all()
        return videos

    def __str__(self):
        return self.title  

class VtubeMerch(models.Model):
    name = models.CharField(max_length = 50)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=10)
    
          