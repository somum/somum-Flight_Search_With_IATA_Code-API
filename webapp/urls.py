from django.contrib import admin
from django.urls import path
from django.urls import path,include
from . import views

urlpatterns = [
    path('index/',views.index,name='index'),
    path('flight_list/',views.flight_list,name='flight_list'),
]
