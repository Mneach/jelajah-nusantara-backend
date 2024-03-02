from rest_framework import serializers

from .models import Content

class ContentExcludedSerializer(serializers.ModelSerializer):
    # Define a serializer for content data with excluded fields
    province_name = serializers.SerializerMethodField()

    class Meta:
        model = Content
        fields = ['id','title', 'image_url', 'province', 'province_name']

    def get_province_name(self, obj):
        if obj.province:
            return obj.province.name
        else:
            return None

class ContentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Content
        fields = ['id','title', 'content', 'image_url']