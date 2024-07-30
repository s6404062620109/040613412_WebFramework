from django.urls import path
from testApp import views

urlpatterns = [
    path("videoform/", views.video_fill, name="videoform"),
    path("authorform/", views.author_fill, name="authorform"),
]
