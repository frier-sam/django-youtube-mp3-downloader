from django.contrib import admin
from django.urls import path,include
from mp3convert import views

urlpatterns = [
    path('convert/', views.convert)
]
