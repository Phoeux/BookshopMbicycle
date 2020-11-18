from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListAPIView
from django.core.paginator import Paginator

from managebook.models import Book
from managebook.serializer import BookSerializer


class ListBook(ListAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        if self.kwargs.get('id'):
            return Book.objects.filter(id=self.kwargs.get('id'))

        return (Book.objects.all())
#
# pag = Paginator(result, 5)
#         response['content'] = pag.page(num_page)
#         response['count_page'] = list(range(1, pag.num_pages + 1))