from rest_framework import serializers
from .models import VtubeMerch

class MerchSerielizer(serializers.ModelSerializer):
    class Meta:
        model = VtubeMerch
        fields = ('id', 'name', 'description', 'price')
        