from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated

from managebook.models import Book, Author
from managebook.serializer import BookSerializer, AuthorSerializer
from rest_framework.views import APIView


class ListBook(ListAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    filter_fields = ['id', 'title', 'author']

    # def get_queryset(self):
    #     if self.kwargs.get('id'):
    #         return Book.objects.filter(id=self.kwargs.get('id'))
    #
    #     return (Book.objects.all())

class CreateBook(CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = BookSerializer


class ListAuthors(ListAPIView):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()


class BoughtBooks(APIView):
    def put(self):
        book = Book.objects



