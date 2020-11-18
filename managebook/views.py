from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListAPIView

from managebook.models import Book
from managebook.serializer import BookSerializer


class ListBook(ListAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    filter_fields = ['id', 'title', 'author']

    # def get_queryset(self):
    #     if self.kwargs.get('id'):
    #         return Book.objects.filter(id=self.kwargs.get('id'))
    #
    #     return (Book.objects.all())
