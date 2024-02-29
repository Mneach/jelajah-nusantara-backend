from django.urls import path
from . import views

urlpatterns = [
    path('getAllIsland/', views.GetIslandAPIView, name="getAllIsland"),
    path('getIslandWithProvincesWithContents/', views.GetIslandWithProvincesWithContentsAPIView, name="getIslandWithProvincesWithContents"),
]
