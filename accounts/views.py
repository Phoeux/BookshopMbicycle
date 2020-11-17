from django.contrib import auth
from django.core.mail import send_mail
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
# from authentication.serializer import UserSerializer, LoginSerializer
from accounts.serialize import UserSerializer, LoginSerializer
from accounts.tasks import send_email_task


class RegisterView(GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            if serializer.user is not None:
                send_email_task.delay(5, serializer)
            #     send_mail('helo lalka', f'{serializer.user.password}', 'lobinsky.gleb@gmail.com', [serializer.user.email],
            #               fail_silently=False)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        data = request.data
        email = data.get('email', '')
        password = data.get('password', '')
        user = auth.authenticate(username=email, password=password)

        if user:
            serializer = UserSerializer(user)

            data = {'user_info': serializer.data, 'password': password}

            return Response(data, status=status.HTTP_200_OK)

        return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
