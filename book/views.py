from django.shortcuts import render, redirect, get_object_or_404
from .forms import mainAuthor, BookStore
from . models import Author, Books
from django.db.models import Q



# Create your views here.
def home(request):
    authors=Author.objects.all()
    books=Books.objects.all()
    return render(request, 'home.html', {'authors':authors, 'books':books,})


def search_books(request):
    query = request.GET.get("q", "")

    books = Books.objects.filter(
        Q(title__iexact=query) |
        Q(author__name__iexact=query))  #Q is use because it handle AND logic and OR logic

    return render(request, "search_results.html", {
        "books": books,
        "query": query,
    })
    
    
def add_author(request):
    if request.method=="POST":
        form=mainAuthor(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
        
    else:
        form=mainAuthor()
    return render(request, 'authors/addAuthor.html', {'form':form})


def update_author(request, pk):
    author_record=get_object_or_404(Author, id=pk)
    if request.method=="POST":
        form=mainAuthor(request.POST, request.FILES, instance=author_record)
        if form.is_valid():
            form.save()
            return redirect('home')    
    else:
        form=mainAuthor(instance=author_record)
    return render(request, 'authors/addAuthor.html', {'form':form})

def delete_author(request, pk):
    author_record=get_object_or_404(Author, id=pk)
    if request.method=="POST":
        author_record.delete()
        return redirect('home')
    return render(request, 'authors/confirm.html', {'form':author_record})
        

def view_author(request, pk):
    author_record=get_object_or_404(Author, id=pk)
    return render(request, 'authors/viewauthor.html', {'author':author_record})


#BOOK PART

def add_book(request):
    if request.method=="POST":
        form=BookStore(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
        
    else:
        form=BookStore()
    return render(request,'books/addbook.html', {'books':form})


def update_book(request, pk):
    book_records=get_object_or_404(Books, id=pk)
    if request.method=="POST":
        form=BookStore(request.POST, instance=book_records)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=BookStore(instance=book_records)
    return render(request, 'books/addbook.html', {'books':form})


def view_book(request, pk):
    book_records=get_object_or_404(Books, id=pk) 
    return render(request, 'books/viewbook.html', {'book':book_records})


def delete_book(request, pk):
    book_records=get_object_or_404(Books, id=pk) 
    if request.method=="POST":
        book_records.delete()
        return redirect('home')
    
    return render(request, 'books/confirm.html', {'book':book_records})