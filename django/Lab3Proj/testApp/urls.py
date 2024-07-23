from django.urls import path
from testApp import views

urlpatterns = [
    path("videoform/", views.video_fill, name="videoform"),
    path("authorform/", views.author_fill, name="authorform"),
    path('author/update/<int:author_id>/', views.author_update, name='author_update'),
    path('author/delete/<int:author_id>/', views.author_delete, name='author_delete'),
]
