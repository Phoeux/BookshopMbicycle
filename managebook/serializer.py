from rest_framework.serializers import ModelSerializer
from managebook.models import User, Book, Author


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class CreateBookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'author']