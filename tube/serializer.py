from rest_framework import serializers
from .models import VtubeInfo

class InfoSerielizer(serializers.ModelSerializer):
    class Meta:
        model = VtubeInfo
        fields = ('id', 'name', 'description')
        