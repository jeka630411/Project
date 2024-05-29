# Ссылки на странички. Каждую новую страницу добавлять сюда
from django.contrib import admin
from django.urls import path, include
from  . import views
urlpatterns = [
    path('',views.index),
    path('about/', views.about, name='about'),
    path('success/', views.success, name='success'),

]
