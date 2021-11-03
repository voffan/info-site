from django.contrib import admin
from django.urls import path
from info import views

urlpatterns = [
    path('', views.index, name='index'),
    path('products', views.products, name='products'),
    path('services', views.services, name='services'),
    path('contacts', views.contacts, name='contacts'),
    path('about', views.about, name='about'),
    path('news', views.news, name='news'),
]
