from django.urls import path, include
from v01 import views


urlpatterns = [
    path('', views.index),
]
