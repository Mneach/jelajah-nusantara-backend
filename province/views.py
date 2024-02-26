from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Province
from .serializers import ProvinceSerializer

# Create your views here.
@api_view(['GET'])
def GetProviceAPIView(request):
    province = Province.objects.all()
    serializer = ProvinceSerializer(province, many=True)
    return Response(serializer.data)