from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics
from .Video import VideoSerializer
from .models import Video


def videoBase(request):
    return render(request, 'base.html')

class VideoAPI(generics.ListCreateAPIView):

    queryset = Video.objects.all()
    serializer_class = VideoSerializer

class VideoAPIPost(generics.ListCreateAPIView):

    queryset = Video.objects.all()
    serializer_class = VideoSerializer

    def post(self, request):

        serializer = VideoSerializer(data=request.POST)

        if serializer.is_valid():
            serializer.save()
            return HttpResponse(serializer.data)
        else:
            return HttpResponse("API POST error")
    