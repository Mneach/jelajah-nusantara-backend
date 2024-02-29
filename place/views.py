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
from .links import aceh_urls

@api_view(['GET'])
def GetAllPlaceDataInProvinceAPIView(request):
    res = scrappingData(aceh_urls)
    return Response(res)

@api_view(['GET'])
def GetPlaceDetailAPIView(request):
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