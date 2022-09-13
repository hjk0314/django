from django.urls import path
from hjk import views


urlpatterns = [
    path('', views.index)
]