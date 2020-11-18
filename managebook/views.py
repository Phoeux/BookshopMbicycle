from django.db.models import Sum
from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from managebook.models import Book, Author, SoldBooks, User
from managebook.serializer import BookSerializer, AuthorSerializer
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication


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
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def put(self, request):
        SoldBooks.objects.create(user_id=request.user.id, book_id=request.data['book_id'],
                                 count=request.data['count'])
        # user = User.objects.get(id=request.data['user_id'])
        return Response(request.user.users_books.aggregate(Sum('count')))


class StatUser(APIView):
    pass


class StatBooks(APIView):
    pass


class DumpBooks(APIView):
    pass
