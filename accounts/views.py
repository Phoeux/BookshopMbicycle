from django.contrib import auth
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
# from authentication.serializer import UserSerializer, LoginSerializer
from accounts.serialize import UserSerializer1, LoginSerializer1


class RegisterView(GenericAPIView):
    serializer_class = UserSerializer1

    def post(self, request):
        serializer = UserSerializer1(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(GenericAPIView):
    serializer_class = LoginSerializer1

    def post(self, request):
        data = request.data
        email = data.get('email', '')
        password = data.get('password', '')
        user = auth.authenticate(username=email, password=password)

        if user:
            serializer = UserSerializer1(user)

            data = {'user': serializer.data}

            return Response(data, status=status.HTTP_200_OK)

        return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
