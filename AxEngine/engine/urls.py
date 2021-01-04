from django.contrib import admin
from django.urls import path
from engine import views

urlpatterns = [
    path("", views.index, name='home'),
    path("search/", views.searchQuery, name='search')
]
