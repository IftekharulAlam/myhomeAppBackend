from django.urls import path

from . import views

urlpatterns = [

    path('getTemparatureData', views.getTemparatureData, name='getTemparatureData'),



]
