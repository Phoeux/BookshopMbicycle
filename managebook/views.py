from datetime import date, timedelta
from django.db.models import Sum, Q
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from managebook.models import Book, Author, SoldBooks, User
from managebook.serializer import BookSerializer, AuthorSerializer, CreateBookSerializer
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication


class ListBook(ListAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    filter_fields = ['id', 'title', 'author']


class CreateBook(CreateAPIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    serializer_class = CreateBookSerializer


class ListAuthors(ListAPIView):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()


class BoughtBooks(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def put(self, request):
        SoldBooks.objects.create(user_id=request.user.id, book_id=request.data['book_id'],
                                 count=request.data['count'])
        return Response(request.user.users_books.aggregate(Sum('count')))


class StatAll(APIView):
    def get(self, request):
        count = Book.objects.aggregate(count=Sum('count'))['count']
        query = Author.objects.all()
        data = {a.name: f'{a.count / count * 100}%' for a in query}
        data['total'] = count
        return Response(data)


class MonthlySoldBooks(APIView):
    def get(self, request):
        today = date.today()
        first_of_this_month = today.replace(day=1)
        lastday_prev_month = first_of_this_month - timedelta(days=1)
        first_day_prev_month = lastday_prev_month.replace(day=1)
        left_query = Q(date__gte=first_day_prev_month)
        right_query = Q(date__lte=lastday_prev_month)
        monthly_countv3 = SoldBooks.objects.filter(left_query & right_query).aggregate(Sum('count'))
        return Response(monthly_countv3)
