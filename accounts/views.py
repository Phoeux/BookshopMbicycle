from django.contrib import auth
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.serialize import UserSerializer, LoginSerializer
from accounts.tasks import send_email_task

User = get_user_model()

class RegisterView(GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            if serializer.user is not None:
                token = Token.objects.create(user=serializer.user)
                send_email_task.delay(5, serializer.data, request.data['password'])
            return Response(f'{token.key}', status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        data = request.data
        email = data.get('email', '')
        password = data.get('password', '')
        user = auth.authenticate(username=email, password=password)

        if user:
            token = Token.objects.get(user=user)
            serializer = UserSerializer(user)

            send_email_task.delay(5, serializer.data, request.data['password'])
            return Response(f'There is your token: {token.key}', status=status.HTTP_200_OK)

        return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class Logout(APIView):
    queryset = User.objects.all()

    def get(self, request, format=None):
        # simply delete the token to force a login
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)