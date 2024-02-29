from rest_framework import serializers
from .models import Province
from content.serializers import ContentSerializer
class ProvinceSerializer(serializers.ModelSerializer):
    contents  = ContentSerializer(many=True, read_only=True)
    class Meta:
        model = Province
        fields = ['id','name', 'latitude', 'longitude', 'image_url', 'contents']