from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Island
from .serializers import IslandSerializer
from django.core import serializers

# Create your views here.
@api_view(['GET'])
def GetIslandAPIView(request):
    province = Island.objects.all()
    serializer = IslandSerializer(province, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def GetIslandWithProvincesWithContentsAPIView(request):
    islands = Island.objects.all()
    serializer = IslandSerializer(islands, many=True)
    return JsonResponse(serializer.data, safe=False)
