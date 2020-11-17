from django.core.mail import send_mail
from celery import shared_task

from time import sleep

from accounts.serialize import UserSerializer


@shared_task
def send_email_task(pause, serializer):
    # serializer = UserSerializer(data=request.data)
    sleep(pause)
    send_mail('helo lalka from celery', f'{serializer.user.name} there is your pass {serializer.user.password}', #f'{serializer.user.name} there is your pass {serializer.user.password}'
              'lobinsky.gleb@gmail.com', [serializer.user.email])
    return None
