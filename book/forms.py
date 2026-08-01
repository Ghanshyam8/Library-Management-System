from django import forms
from . models import Author, Books

class mainAuthor(forms.ModelForm):
    class Meta:
        model = Author
        fields=['name', 'description']

class BookStore(forms.ModelForm):
    class Meta:
        model= Books
        fields= '__all__'