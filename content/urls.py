from django.urls import path
from . import views

urlpatterns = [
    path('getAllContentDataInAllProvince/', views.GetAllContentDataInAllProvinceAPIView, name="getAllContentDataInAllProvince"),
    path('getContentDetail/', views.GetContentDetailAPIView, name="getPlaceDetail"),
    path('getAllContentDataInProvince/', views.GetAllContentDataInProvinceAPIView, name="getAllPlaceDataInProvince"),
    path('insertContent/' , views.InsertContent, name="insertContent"),
    path('insertALLPlaceContent/', views.InsertALLPlaceContent, name="insertALLPlaceContent")
]
