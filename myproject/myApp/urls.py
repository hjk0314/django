from django.contrib import admin
from django.urls import path
from myproject.myApp import views


urlpatterns = [
    path("", views.index), 
    path("cal/", views.cal), 
]
