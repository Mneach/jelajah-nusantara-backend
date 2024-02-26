from django.urls import path
from . import views

urlpatterns = [
    path('getNews/', views.GetNews, name="getNews"),
    path('getNewsDetail/', views.GetNewsDetail, name='getNewsDetail'),
]
