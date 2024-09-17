from django.shortcuts import render
from .models import *
from .forms import UserForm

# Create your views here.

def user_fill(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            u = User(
                Citizenid=form.cleaned_data['Citizenid'],
                Firstname=form.cleaned_data['Firstname'],
                Lastname=form.cleaned_data['Lastname'],
                Expire_date=form.cleaned_data['ExpireDate'],
                Blood_type=form.cleaned_data['Blood_type'],
            )
            u.save()
            context = {"User": f"{u.Firstname} {u.Lastname}", "Blood Type": u.Blood_type}
            return render(request, "thanks.html", context)
    else:
        form = UserForm()
    return render(request, "base.html", {"form": form})