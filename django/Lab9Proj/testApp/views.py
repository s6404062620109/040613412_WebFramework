from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.sessions.backends.db import SessionStore
from django.contrib.sessions.models import Session
from .forms import LoginForm
from .models import Author, Member, Video

def login_fill(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            try:
                m = Member.objects.get(username=username, password=password)
            except Member.DoesNotExist:
                return HttpResponse("Can't login. Invalid credentials.")

            request.session['member_id'] = m.id
            request.session['member_firstname'] = m.firstname

            s = SessionStore()
            s.create()
            keysession = s.session_key

            request.session['session_key'] = keysession

            s['member_id'] = m.id
            s['member_firstname'] = m.firstname
            s.save()

            return redirect("../showvideo/")
        
        else:
            return render(request, "login.html", {"form": form})

    else:
        form = LoginForm()
        return render(request, "login.html", {"form": form})
    
def logOut(request):

    try:
        member = request.session["member_firstname"]

        del request.session["member_id"]
        del request.session["member_firstname"]
        del request.session["session_key"]

        session_key = request.session.session_key
        if session_key:
            Session.objects.filter(session_key=session_key).delete()
        request.session.flush()  

    except KeyError:
        pass

    return redirect("/login/")

def showvideo(request):

    member_firstname = request.session.get('member_firstname', 'Guest')
    videos = Video.objects.all()
    session_key = request.session.session_key

    context = {
        'member_firstname': member_firstname,
        'videos': videos,
        'session_key': session_key, 
    }

    return render(request, 'showvideo.html', context)

def showauthor(request):

    member_firstname = request.session.get('member_firstname', 'Guest')
    authors = Author.objects.all()
    session_key = request.session.session_key

    context = {
        'member_firstname': member_firstname,
        'authors': authors,
        'session_key': session_key, 
    }
    return render(request, 'showauthor.html', context)
