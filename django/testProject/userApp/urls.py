from django.urls import path
from userApp import views

urlpatterns = [
    path('', views.index),
    path('signin/', views.signIn),
    path('videos/', views.Video_list),
    path('author/', views.Author_list),
]
