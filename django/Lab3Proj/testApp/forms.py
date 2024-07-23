from django import forms
from .models import Author

class VideoForm(forms.Form):

    title = forms.CharField(label="Video title", max_length=50)
    publish = forms.DateField(label="Published date")
    short_detail = forms.CharField(label="Short detail", max_length=250)
    demo = forms.BooleanField(initial=False)

class AuthorForm(forms.Form):

    id = forms.CharField(label="Id", max_length=13)
    firstname = forms.CharField(label="Firstname", max_length=255)
    lastname = forms.CharField(label="Lastname", max_length=255)
    phone = forms.CharField(label="Phone", max_length=10)
    joined_date = forms.DateField()
    type = forms.ChoiceField(label="Type", choices=Author.AUTHOR_TYPE_CHOICES)