from django.urls import path
from intro import views


urlpatterns = [
    path('', views.index),
]
