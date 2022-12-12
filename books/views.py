from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView,DetailView,UpdateView
from django.views.generic.edit import CreateView,DeleteView
from django.urls import reverse_lazy
from .models import Book
# Create your views here.

class BookList(ListView):
    model = Book

class BookView(DetailView):
    model = Book

class BookCreate(CreateView):
    model = Book
    fields = "__all__"
    success_url = reverse_lazy('book_list')

class BookUpdate(UpdateView):
    template_name = 'books/book_edit_form.html'
    model = Book
    fields = "__all__"
    success_url = reverse_lazy('book_list')

class BookDelete(DeleteView):
    model = Book
    success_url = reverse_lazy('book_list')






