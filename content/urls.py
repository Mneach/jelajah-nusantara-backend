from django.urls import path
from . import views

urlpatterns = [
    path('getAllContentDataInAllProvince/', views.GetAllContentDataInAllProvinceAPIView, name="getAllContentDataInAllProvince"),
    path('getAllContentDataInProvince/', views.GetAllContentDataInProvinceAPIView, name="getAllPlaceDataInProvince"),
    path('insertContent/' , views.InsertContent, name="insertContent"),
    path('insertALLPlaceContent/', views.InsertALLPlaceContentAPIView, name="insertALLPlaceContent"),
    path('insertALLFoodsContent/', views.InsertALLFoodsContentAPIView, name="insertALLFoodsContent"),
    path('insertALLCulturesContent/', views.InsertALLCulturesContentAPIView, name="insertALLCulturesContent"),
    path('getContentDetail/<str:title>/', views.GetContentDetailAPIView, name="getContentDetailAPIView")
]
