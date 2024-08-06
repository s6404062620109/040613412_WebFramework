from datetime import date
from django import forms
from .models import Author,Video

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ["id","firstname", "lastname", "phone", "joined_date"]
        today = date.today()
        widgets= {"id": forms.TextInput(attrs={"size": 30 }),
                    "firstname": forms.TextInput(attrs={"size": 30 }),
                    "lastname": forms.TextInput(attrs={"size": 30 }),
                    "phone": forms.TextInput(attrs={"size": 30 }),
                    "joined_date" : forms.DateInput(attrs={"format": "%Y-%m-%d",
                    "value": today }),
                }

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ["title", "published_date", "author"]
        today = date.today()
        widgets = {
            "title": forms.TextInput(attrs={"size": 50}),
            "published_date": forms.DateInput(attrs={"format": "%Y-%m-%d", "value": today}),
            "author": forms.Select(),
        }