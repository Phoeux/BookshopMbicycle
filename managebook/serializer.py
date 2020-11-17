from rest_framework.serializers import ModelSerializer

from managebook.models import User, Book


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
