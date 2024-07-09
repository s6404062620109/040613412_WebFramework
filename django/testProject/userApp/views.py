from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import *


# Create your views here.
def index (request):
    return render(request, "index.html")

def signIn (request):
    return render(request, "signIn.html")

def Video_list (request):
    Videos = Video.objects.all()
    template = loader.get_template("videos.html")
    context = {
        'videos': Videos
    }
    return HttpResponse(template.render(context, request))

def Author_list (request):
    Authors = Author.objects.all()
    template = loader.get_template("author.html")
    context = {
        'authors': Authors
    }
    return HttpResponse(template.render(context, request))