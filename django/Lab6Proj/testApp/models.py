from django.db import models

# Create your models here.

class Author(models.Model):

    id = models.CharField(primary_key = True, max_length=13, auto_created=False)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone = models.CharField(max_length=10)
    joined_date = models.DateField()

class Books(models.Model):
    CATEGORY_TYPE_CHOICES = [
        ('Default', 'Default'),
        ('Action', 'Action'),
        ('Survey', 'Survey'),
        ('Fantasy', 'Fantasy'),
    ]

    id = models.CharField(primary_key = True, max_length=13, auto_created=False)
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=10, choices=CATEGORY_TYPE_CHOICES, default='Default')
    saleprice = models.IntegerField(default=0)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
