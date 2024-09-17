from django.db import models

# Create your models here.
class User(models.Model):
    BLOOD_TYPE_CHOICES = [
        ('o', 'O'),
        ('a', 'A'),
        ('b', 'B'),
        ('ab', 'AB')
    ]

    Citizenid = models.CharField(primary_key = True, max_length=13, auto_created=False)
    Firstname = models.CharField(max_length=255)
    Lastname = models.CharField(max_length=255)
    Expire_date = models.DateField()
    Blood_type = models.CharField(max_length=5, choices=BLOOD_TYPE_CHOICES, default='o')