from rest_framework import serializers
from .models import Province
from content.serializers import ContentExcludedSerializer
class ProvinceSerializer(serializers.ModelSerializer):
    contents  = ContentExcludedSerializer(many=True, read_only=True)
    class Meta:
        model = Province
        fields = ['id','name', 'latitude', 'longitude', 'image_url', 'contents']