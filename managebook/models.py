from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):
    email = models.EmailField(max_length=40, unique=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    phone_number = PhoneNumberField(max_length=20, help_text='Contact phone number')
    address = models.CharField(max_length=20, blank=True, help_text='Please enter your current living address',
                               verbose_name='Address')
    city = models.CharField(max_length=20, blank=True, help_text='Please enter your city', verbose_name='City')


class Author(models.Model):
    name = models.CharField(max_length=50)


class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
