from django.shortcuts import render
from django.views.generic import ListView
from .models import Book

# Create your views here.

class BookList(ListView):
    template_name='main/list.html'
    def get_queryset(self):
        query=self.request.GET.get('search')
        qs=Book.objects.all()
        if query:
            query=query.strip()
            qs = qs.search(query)
        return qs