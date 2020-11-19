from django.core.mail import send_mail
from celery import shared_task
from time import sleep


@shared_task
def send_email_task(pause, serializer, password):
    sleep(pause)
    send_mail('helo lalka from celery', f'{serializer["username"]} there is your pass {password}',
              'lobinsky.gleb@gmail.com', [serializer["email"]])
    return None
