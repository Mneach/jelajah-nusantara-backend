from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from bs4 import BeautifulSoup
from requests import get
from news.utils import extractFindAllData
from .utils import scrappingData
from .place_links import province_place_urls
from .models import Content
from province.models import Province

@api_view(['POST'])
def InsertALLPlaceContent(request):
    content_type = 'place',

    for province_name, urls in province_place_urls.items():
        print(f"Province: {province_name}")
        province_id = Province.objects.filter(name=province_name).first().id
        datas = scrappingData(urls)
        for data in datas:
            Content.objects.create(
                title= data.get("title"),
                content = data.get('content'),
                image_url = data.get('image_url'),
                content_type = content_type,
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

@api_view(['GET'])
def GetContentDetailAPIView(request):
    data = []
    try:
        url = get(request.GET.get('url', ''))
        soup = BeautifulSoup(url.text, 'html.parser')
        content_container = soup.find('main', class_="mw-body")
        title = soup.find('span', class_="mw-page-title-main").text
        content = content_container.findAll(lambda tag: tag.name == 'p' and not tag.attrs)
        # image_container = soup.find('table', class_="infobox vcard")
        image_url = content_container.find('img', class_="mw-file-element").get('src')
        print(image_url)
        data.append({
            "title": title,
            "content": extractFindAllData(content),
            "image_url" : image_url,
        })
    except Exception as error:
        print(error)
        data.append({
            "message": "error!",
        })

    return Response(data[0])