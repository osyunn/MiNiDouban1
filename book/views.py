from django.shortcuts import render
from django.core.paginator import Paginator
# Create your views here.
from django.shortcuts import render
from .models import Book
from django.shortcuts import get_object_or_404

def bookhome(request):
    searchTerm = request.GET.get('searchBook')
    if searchTerm:
        book_list = Book.objects.filter(title__contains=searchTerm)
    else:
        book_list = Book.objects.all()
    paginator = Paginator(book_list, 3)
    page_number = request.GET.get('page', 1)
    books = paginator.page(page_number)
    return render(request, 'bookhome.html', {'searchTerm':searchTerm, 'books':books})

def bookdetail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'bookdetail.html', {'book': book})


