from django.urls import path

from . import views

urlpatterns = [

    path('sendTempHumData', views.sendTempHumData, name='sendTempHumData'),
    path('getTemparatureDataApp', views.getTemparatureDataApp,name='getTemparatureDataApp'),

]
