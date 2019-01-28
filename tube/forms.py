from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class NewVideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['title', 'videofile']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['video']