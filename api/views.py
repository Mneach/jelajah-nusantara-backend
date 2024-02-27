from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
import feedparser

@api_view(['GET'])
def getAllNews(request):
    if request.method == 'GET':
        feed = feedparser.parse("https://www.cnnindonesia.com/rss")

        return Response(feed.entries)