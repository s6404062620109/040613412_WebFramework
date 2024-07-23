from django.shortcuts import render, get_object_or_404, redirect

from .models import Author, Video
from .forms import VideoForm, AuthorForm

# Create your views here.
def video_fill(request):
    if request.method == "POST":
        form = VideoForm(request.POST)
        if form.is_valid():
            v = Video(
                title=form.cleaned_data['title'],
                published_date=form.cleaned_data['publish'],
                short_detail=form.cleaned_data['short_detail'],
                demo=form.cleaned_data['demo'],
            )
            v.save()
            context = {"title": v.title, "published_date": v.published_date}
            return render(request, "thanks.html", context)
    else:
        form = VideoForm()
    return render(request, "videoform.html", {"form": form})

def author_fill(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            a = Author(
                id=form.cleaned_data['id'],
                firstname=form.cleaned_data['firstname'],
                lastname=form.cleaned_data['lastname'],
                phone=form.cleaned_data['phone'],
                joined_date=form.cleaned_data['joined_date'],
                type_author=form.cleaned_data['type'],
            )
            a.save()
            context = {"Fullname": f"{a.firstname} {a.lastname}", "phone": a.phone}
            return render(request, "thanks.html", context)
    else:
        form = AuthorForm()
    return render(request, "authorform.html", {"form": form})

def author_update(request, author_id):
    author = get_object_or_404(Author, id=author_id)
    
    if request.method == "POST":
        form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            form.save()
            return redirect('Author Update Success')  
    else:
        form = AuthorForm(instance=author)
    
    return render(request, 'authorform.html', {'form': form})

def author_delete(request, author_id):
    author = get_object_or_404(Author, id=author_id)
    
    if request.method == "POST":
        author.delete()
        return redirect('Author Delete Success')  

    return render(request, 'authorform.html', {'author': author})