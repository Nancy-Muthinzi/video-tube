from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class NewVideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['title', 'videofile']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['video']