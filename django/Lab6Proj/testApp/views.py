from django.shortcuts import render
from .models import Author, Books

# Create your views here.

def get_all_books_and_authors(request):
    books_with_authors = Books.objects.select_related('author').all()

    context = {
        'books_with_authors': books_with_authors,
    }

    return render(request, 'Booklist.html', context)