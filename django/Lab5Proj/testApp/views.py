from django.forms import modelformset_factory

from django.http import HttpResponse
from django.shortcuts import render
from .models import Author,Video
from .forms import AuthorForm,VideoForm

#Example form ser view
def authorformset(request):
    AuthorFormSet = modelformset_factory(Author, form = AuthorForm , extra=2)
    if request.method == "POST":
        formset = AuthorFormSet(request.POST)
        if formset.is_valid():
            formset.save()
            return HttpResponse('Thanks....Save formset already.') #This can be template
        else:
        #Raised error
            return HttpResponse('ERROR formset !')
    else:
        formset = AuthorFormSet()
        queryfirstname = Author.objects.filter(firstname__startswith="A")
        context = {
            "formset": formset,
            "queryfirstname": queryfirstname
        }
    return render(request, "addauthorsformset.html", context)

def authorform(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            a = Author(
                id=form.cleaned_data['id'],
                firstname=form.cleaned_data['firstname'],
                lastname=form.cleaned_data['lastname'],
                phone=form.cleaned_data['phone'],
                joined_date=form.cleaned_data['joined_date'],
            )
            a.save()
            return HttpResponse('Thanks....Save formset already.')
    else:
        form = AuthorForm()
        queryfirstname = Author.objects.filter(firstname__startswith="A")
        context = {
            "form": form,
            "queryfirstname": queryfirstname
        }
    return render(request, "addauthorsform.html", context)

def videoform(request):
    if request.method == "POST":
        form = VideoForm(request.POST)
        if form.is_valid():
            a = Video(
                title=form.cleaned_data['title'],
                published_date=form.cleaned_data['published_date'],
                author=form.cleaned_data['author'],
            )
            a.save()
            return HttpResponse('Thanks....Save formset already.')
    else:
        form = VideoForm()
        queryfirstname = Video.objects.filter(title__startswith="A")
        context = {
            "form": form,
            "queryfirstname": queryfirstname
        }
    return render(request, "addvideoform.html", context)
