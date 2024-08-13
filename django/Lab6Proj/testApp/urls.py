from django.urls import path
from .views import *

urlpatterns = [
    path('', get_all_books_and_authors),
]