from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Province
from .serializers import ProvinceSerializer

# Create your views here.



@api_view(['GET'])
def GetProvinceAPIView(request):
    province = Province.objects.all()
    serializer = ProvinceSerializer(province, many=True)
    return Response(serializer.data)

def GetProvinceWithIslands(request):
    provinces = Province.objects.select_related('island').all() 
    serializer = ProvinceSerializer(provinces, many=True)
    print(serializer.data)
    return JsonResponse(serializer.data, safe=False)