from django.shortcuts import render, redirect
from .forms import mainAuthor, BookStore, Author, Books


# Create your views here.
def home(request):
    authors=Author.objects.all()
    books=Books.objects.all()
    return render(request, 'home.html', {'authors':authors, 'books':books,})


def add_author(request):
    if request.method=="POST":
        form=mainAuthor(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
        
    else:
        form=mainAuthor()
    return render(request, 'addAuthor.html', {'authors':form})





def add_book(request):
    if request.method=="POST":
        form=BookStore(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
        
    else:
        form=BookStore()
    return render(request,'books/addbook.html', {'books':form})