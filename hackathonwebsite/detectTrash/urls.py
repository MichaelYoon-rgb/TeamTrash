from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('getLocations', views.getLocations, name='getLocations'),
    path('setLocations', views.setLocations, name='setLocations')
]