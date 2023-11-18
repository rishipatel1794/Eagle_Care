from django.contrib import admin
from django.urls import path
from medicine import views

urlpatterns = [
    path("",views.index,name="home"),
    path("search/", views.search,name="search"),
]