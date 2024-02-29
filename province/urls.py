from django.urls import path
from . import views

urlpatterns = [
    path('getProvince/', views.GetProvinceAPIView, name="getProvince"),
    path('getProvinceWithIslands/', views.GetProvinceWithIslands, name="getProvinceWithIsland")
]
