from rest_framework import serializers

from .models import Content

class ContentExcludedSerializer(serializers.ModelSerializer):
    # Define a serializer for content data with excluded fields
    class Meta:
        model = Content
        exclude = ['content', 'province']

class ContentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Content
        fields = ['id','title', 'content', 'image_url']