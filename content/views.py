from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .utils import scrappingData
from .place_links import province_place_urls
from .food_links import province_food_urls
from .culture_links import province_culture_urls
from .models import Content
from province.models import Province
from .serializers import ContentSerializer

@api_view(['POST'])
def InsertALLCulturesContentAPIView(request):
    for province_name, urls in province_culture_urls.items():
        print(f"Culture From Province : {province_name}")
        province_id = Province.objects.filter(name=province_name).first().id
        datas = scrappingData(urls, "Culture")
        for data in datas:
            Content.objects.create(
                title= data.get("title"),
                content = data.get('content'),
                image_url = data.get('image_url'),
                content_type = "Culture",
                province_id = province_id
            )
        print(f"Successfully Insert Culture From Province : {province_name}")            

    return Response("Success")

@api_view(['POST'])
def InsertALLFoodsContentAPIView(request):
    for province_name, urls in province_food_urls.items():
        print(f"Food From Province : {province_name}")
        province_id = Province.objects.filter(name=province_name).first().id
        datas = scrappingData(urls, "Food")
        for data in datas:
            Content.objects.create(
                title= data.get("title"),
                content = data.get('content'),
                image_url = data.get('image_url'),
                content_type = "Food",
                province_id = province_id
            )
        print(f"Successfully Insert Food From Province : {province_name}")            

    return Response("Success")

@api_view(['POST'])
def InsertALLPlaceContentAPIView(request):
    for province_name, urls in province_place_urls.items():
        print(f"Province: {province_name}")
        province_id = Province.objects.filter(name=province_name).first().id
        datas = scrappingData(urls, "Place")
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
    datas = scrappingData(province_urls, "Place")

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
def GetContentDetailAPIView(request, title):
    place_title = title.replace("-", " ")
    place = Content.objects.filter(title=place_title).first()
    serializer = ContentSerializer(place)
    return Response(serializer.data)

@api_view(['GET'])
def GetAllContentDataInAllProvinceAPIView(request):

    res = []

    for province, urls in province_place_urls.items():
        print(f"Province: {province}")
        data = scrappingData(urls, "Place")
        res.append(data)

    return Response(res)

@api_view(['GET'])
def GetAllContentDataInProvinceAPIView(request):
    province_name = request.GET.get('province_name')
    province_urls = province_place_urls[province_name]
    res = scrappingData(province_urls, "Place")
    return Response(res)