from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('addauthor/', views.add_author, name='addauthor'),
    path('addbook/', views.add_book, name='addbook'),
]
