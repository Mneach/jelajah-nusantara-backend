import feedparser
from bs4 import BeautifulSoup
from requests import get
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse
from .utils import extractFindAllData


@api_view(['GET'])
def GetAllNews(request):
    if request.method == 'GET':
        feed = feedparser.parse("https://www.cnnindonesia.com/rss")

        return Response(feed.entries)

@api_view(['GET'])
def GetNewsDetail(request):
    if request.method == 'GET':
        data = []
        try:
            url = get(request.GET.get('url', ''))
            soup = BeautifulSoup(url.text, 'html.parser')
            content_container = soup.find('div', class_="grow-0 w-leftcontent min-w-0")
            title = content_container.find('h1', class_="mb-2 text-[28px] leading-9 text-cnn_black").text
            publish = content_container.find('div', class_="text-cnn_grey text-sm mb-4").text
            description_container = content_container.find('div', class_= lambda x: x and 'detail-text' in x.split() and 'text-cnn_black' in x.split())
            description = description_container.findAll(lambda tag: tag.name == 'p' and not tag.attrs)
            photo = content_container.find('div', class_='detail-image my-5')

            if photo:
                photo = photo.find("img").get("src")
            else:
                photo = soup.find("meta", {"name" : "dtk:thumbnailUrl"}).get("content")

            data.append({
                "title": title,
                "publish": publish,
                "photo" : photo,
                "description": extractFindAllData(description),
            })
        except Exception as error:
            print(error)
            data.append({
                "message": "error!",
            })

        return Response(data[0])