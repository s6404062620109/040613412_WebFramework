from django.urls import path
from testApp import views

urlpatterns = [
    path("showvideo/<str:video_title>/", views.show_video.as_view(), name = "showvideo"),
    path("showcoursevideo/<int:course_id>/",views.show_coursevideo.as_view(), name="showcourse"),
]
