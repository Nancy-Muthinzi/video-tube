from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from pyuploadcare.dj.models import FileField

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    profile_pic = models.ImageField(upload_to='profile/')
    bio = models.CharField(max_length=500, blank=True)
    email = models.EmailField()
    video = models.ForeignKey('Video', blank=True, null=True)
    
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
        try:
            instance.profile.save()
        except ObjectDoesNotExist:
            Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    def update_profile(request, user_id):
        user = User.objects.get(pk=user_id)
        user.profile.bio = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit...'    
        user.save

    def __str__(self):
        return self.first_name + " " + self.last_name

    class Meta:
        ordering = ['first_name', 'last_name']

class Video(models.Model):
    title = models.CharField(max_length = 50)    
    videofile = models.FileField(upload_to='videos/', null=True, verbose_name="")   
    link = models.URLField(blank=True)
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

class Post(models.Model):
    user = models.ForeignKey(Profile, related_name='profile')
    post = models.CharField(max_length = 150)
    video = models.ForeignKey(Video, related_name='posts')        

class VtubeInfo(models.Model):
    name = models.CharField(max_length = 50)
    description = models.TextField()



