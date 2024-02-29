from rest_framework import serializers
from .models import Island
from province.serializers import ProvinceSerializer

class IslandSerializer(serializers.ModelSerializer):
    provinces  = ProvinceSerializer(many=True, read_only=True)

    class Meta:
        model = Island
        fields = ['id', 'name', 'latitude', 'longitude', 'image_url','provinces']