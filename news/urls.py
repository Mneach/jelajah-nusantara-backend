from django.urls import path
from . import views

urlpatterns = [
    path('getAllNews/', views.GetAllNews, name="getAllNews"),
    path('getNewsDetail/', views.GetNewsDetail, name='getNewsDetail'),
]
