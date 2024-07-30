from django.db import models

# Create your models here.
class Author(models.Model):
    AUTHOR_TYPE_CHOICES = [
        ('Fulltime', 'fulltime'),
        ('Parttime', 'parttime'),
    ]

    id = models.CharField(primary_key = True, max_length=13, auto_created=False)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone = models.CharField(max_length=10, blank = True)
    joined_date = models.DateField()
    type_author = models.CharField(max_length=10, choices=AUTHOR_TYPE_CHOICES, default='Fulltime')

    def __str__(self):
        return f'{self.firstname} {self.lastname}'

class Video(models.Model):

    title = models.CharField(max_length=50)
    published_date = models.DateField(null=True)
    short_detail = models.CharField(max_length = 300)
    demo = models.BooleanField(default= False)
    
    def __str__(self):
        return f'{self.title} {self.id}'
    