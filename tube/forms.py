from django import forms
from .models import Video

class NewVideoForm(forms.ModelForm):
    class Meta:
        model = Video
        exclude = ['merchant']
