from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path,include
from . import views

urlpatterns = [
    path('index/',views.index,name='index'),
    path('flight_list/',views.flight_list,name='flight_list'),
]

urlpatterns = format_suffix_patterns(urlpatterns)