from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('addauthor/', views.add_author, name='addauthor'),
    path('updateauthor/<int:pk>/', views.update_author, name='editauthor'),
    path('deleteauthor/<int:pk>/', views.delete_author, name='deleteauthor'),
    path('viewauthor/<int:pk>/', views.view_author, name='viewauthor'),
    
    path("search/", views.search_books, name="search"),
    
    path('addbook/', views.add_book, name='addbook'),
    path('updatebook/<int:pk>/', views.update_book, name='editbook'),
    path('viewbook/<int:pk>/', views.view_book, name='viewbook'),
    path('deletebook/<int:pk>/', views.delete_book, name='deletebook'),
    
]
