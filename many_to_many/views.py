from django.shortcuts import render
from .models import Author, Book
# Create your views here.
def manytomany(request):
    authors = Author.objects.all()
    books = Book.objects.all()

    context = {
        'authors':authors, 
        'books': books,  
    }
    return render(request, 'many-to-many.html', context)
