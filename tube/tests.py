from django.test import TestCase
from .models import Video

# Create your tests here.
class VideoTestClass(TestCase):
    def setUp(self):
        self.new_video = Video(Title = 'Test Video', Post = 'Video Info')
        self.new_video.save()

        self.new_video.add(self)

    def tearDown(self):
        Video.objects.all().delete()