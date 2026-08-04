from django.db import models
from PIL import Image


# Create your models here.
class Author(models.Model):
    photo=models.ImageField(upload_to='media/', blank=True, null=True)
    name=models.CharField(max_length=100)
    description = models.TextField()
    
    def __str__(self):
        return self.name
    
    
class Books(models.Model):
    author=models.ForeignKey(Author, on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    published_date=models.DateField(auto_now_add=False)
    available=models.BooleanField(default=True)
    
    
    