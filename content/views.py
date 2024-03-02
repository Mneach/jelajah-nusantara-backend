from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .utils import scrappingData
from .place_links import province_place_urls
from .models import Content
from province.models import Province
from .serializers import ContentSerializer

@api_view(['POST'])
def InsertALLFoodsContentAPIView(request):
    for province_name, urls in province_place_urls.items():
        print(f"Province: {province_name}")
        province_id = Province.objects.filter(name=province_name).first().id
        datas = scrappingData(urls)
        for data in datas:
            Content.objects.create(
                title= data.get("title"),
                content = data.get('content'),
                image_url = data.get('image_url'),
                content_type = "Place",
                province_id = province_id
            )

    return Response("Success")

@api_view(['POST'])
def InsertALLPlaceContentAPIView(request):
    for province_name, urls in province_place_urls.items():
        print(f"Province: {province_name}")
        province_id = Province.objects.filter(name=province_name).first().id
        datas = scrappingData(urls)
        for data in datas:
            Content.objects.create(
                title= data.get("title"),
                content = data.get('content'),
                image_url = data.get('image_url'),
                content_type = "Place",
                province_id = province_id
            )

    return Response("Success")

@api_view(['POST'])
def InsertContent(request):
    # GET DATA FROM BODY
    content_type = request.data.get('content_type')
    province_name = request.data.get('province_name')

    # GET PROVINCE ID BY NAME
    province_id = Province.objects.filter(name=province_name).first().id

    # GET PROVINCE URLS
    province_urls = province_place_urls[province_name]

    # SCRAPPING DATA
    datas = scrappingData(province_urls)

    # INSERT INTO DATABASE
    for data in datas:
        Content.objects.create(
            title= data.get("title"),
            content = data.get('content'),
            image_url = data.get('image_url'),
            content_type = content_type,
            province_id = province_id
        )
    
    return Response("success")

@api_view(['GET'])
def GetContentDetailAPIView(request):
    place_title = request.GET.get('title')
    place = Content.objects.filter(title=place_title).first()
    serializer = ContentSerializer(place)
    return Response(serializer.data)

@api_view(['GET'])
def GetAllContentDataInAllProvinceAPIView(request):

    res = []

    for province, urls in province_place_urls.items():
        print(f"Province: {province}")
        data = scrappingData(urls)
        res.append(data)

    return Response(res)

@api_view(['GET'])
def GetAllContentDataInProvinceAPIView(request):
    province_name = request.GET.get('province_name')
    province_urls = province_place_urls[province_name]
    res = scrappingData(province_urls)
    return Response(res)