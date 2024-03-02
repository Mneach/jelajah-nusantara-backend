from django.urls import path
from . import views

urlpatterns = [
    path('getScrappingFoodLinks/', views.GetScrappingFoodLinksAPIView, name="getScrappingFoodLinks"),
    path('getScrappingCultureLinks/', views.GetScrappingCultureLinksAPIView, name="getScrappingCultureLinks"),
    path('getScrappingDetail/', views.GetScrappingDetailAPIView, name="getScrappingDetail")
]
