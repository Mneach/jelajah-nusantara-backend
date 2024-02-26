from django.urls import path
from . import views

urlpatterns = [
    path('getProvince/', views.GetProviceAPIView, name="getProvince")
]
