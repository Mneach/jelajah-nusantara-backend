from django.urls import path
from . import views

urlpatterns = [
    path('getPlaceDetail/', views.GetPlaceDetailAPIView, name="getPlaceDetail"),
    path('getAllPlaceDataInProvince/', views.GetAllPlaceDataInProvinceAPIView, name="getAllPlaceDataInProvince")
]
