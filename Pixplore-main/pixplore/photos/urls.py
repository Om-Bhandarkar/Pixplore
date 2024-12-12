
from django.contrib import admin
from django.urls import path
from photos import views

app_name = 'photos'

urlpatterns = [
    path('', views.search_photos_page, name='search_photos_page'),
    path('about/', views.about, name='about'),
]
