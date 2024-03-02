from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from bs4 import BeautifulSoup
from requests import get
from content.utils import generateImageByCategory
from news.utils import extractFindAllData

# Create your views here.
@api_view(['GET'])
def GetScrappingFoodLinksAPIView(request):

    url = get("https://id.wikipedia.org/wiki/Daftar_masakan_Indonesia#Makanan")
    soup = BeautifulSoup(url.text, 'html.parser')
    content_container = soup.findAll('div', attrs={'style': 'column-count:3; column-gap:10px; -moz-column-count:3; -moz-column-gap:10px; -webkit-column-count:3; -webkit-column-gap:10px;'})

    res = []
    for contents in content_container:
        links = contents.find_all('a')
        for link in links:
            if 'new' not in link.get('class', []):
                href = link.get('href')
                res.append(href)

    return Response(res)

@api_view(['GET'])
def GetScrappingCultureLinksAPIView(request):

    url = get("https://id.wikipedia.org/wiki/Daftar_Warisan_Budaya_Takbenda_Indonesia")
    soup = BeautifulSoup(url.text, 'html.parser')
    content_container = soup.find('div', class_="mw-content-ltr mw-parser-output")
    title_container = content_container.findAll('h3')
    table_container = content_container.findAll('table', class_="wikitable")

    titles = []
    for container in title_container:
        title = container.find('span', class_="mw-headline")
        titles.append(title.text)


    res = []
    for index, container in enumerate(table_container):
        if index >= len(titles) : break
        title = titles[index]
        linkData = []
        links = container.find_all('a')
        for link in links:
            if 'new' not in link.get('class', []):
                href = link.get('href')
                linkData.append(href)

        entry = {'title': title, 'links': linkData}
        res.append(entry)

    print(res)
    return Response(res)


@api_view(['GET'])
def GetScrappingDetailAPIView(request):
    data = []
    try:
        url = get(request.GET.get('url', ''))
        soup = BeautifulSoup(url.text, 'html.parser')
        content_container = soup.find('main', class_="mw-body")
        title = soup.find('span', class_="mw-page-title-main").text
        content = content_container.findAll(lambda tag: tag.name == 'p' and not tag.attrs)
        image_url = content_container.find('img', class_="mw-file-element").get('src')
        content = "\n".join(extractFindAllData(content))

        image_url = generateImageByCategory(content)
        data.append({
            "title": title,
            "content": content,
            "image_url" : image_url,
        })
    except Exception as error:
        print(error)
        data.append({
            "message": "error!",
        })

    return Response(data[0])