from django.urls import path
from testApp import views

urlpatterns = [
    path('addauthorsformset/', views.authorformset , name='addauthorsformset'),
    path('addauthorsform/', views.authorform , name='addauthorsform'),
    path('addvideoform/', views.videoform , name='addvideoform'),
]