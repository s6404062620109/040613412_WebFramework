from django import forms
from django.core.exceptions import ValidationError
from datetime import date
from .models import User

class UserForm(forms.Form):
    Citizenid = forms.CharField(label="Citizenid", max_length=13)
    Firstname = forms.CharField(label="Firstname", max_length=255)
    Lastname = forms.CharField(label="Lastname", max_length=255)
    ExpireDate = forms.DateField()
    Blood_type = forms.ChoiceField(label="Blood Type", choices=User.BLOOD_TYPE_CHOICES)
    def clean_Citizenid(self):
        citizenid = self.cleaned_data['Citizenid']
        if not citizenid.isdigit():
            raise ValidationError("Citizen ID must contain only numbers.")
        if citizenid[0] == '0':
            raise ValidationError("Citizen ID must not start with zero.")
        if len(citizenid) != 13:
            raise ValidationError("Citizen ID must be exactly 13 characters long.")
        return citizenid

    def clean(self):
        cleaned_data = super().clean()
        firstname = cleaned_data.get('Firstname')
        lastname = cleaned_data.get('Lastname')
        print(firstname)
        print(lastname)
        # Validate Firstname and Lastname are not the same
        if firstname and lastname and firstname == lastname:
            raise ValidationError({'Firstname': "First Name and Last Name cannot be the same."})
        return self.cleaned_data

    def clean_ExpireDate(self):
        cleaned_data = super().clean()
        expire_date = cleaned_data.get('ExpireDate')
        print(expire_date)

        # Validate Expire_date is not earlier than today
        if expire_date and expire_date < date.today():
            raise ValidationError("Expire date must not be earlier than today's date.")
        return expire_date