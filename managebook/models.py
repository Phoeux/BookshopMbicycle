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
    count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='authors_books')
    buyers = models.ManyToManyField(User, through='managebook.SoldBooks', blank=True, related_name='bought_books')
    count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title


class SoldBooks(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='users_books')
    book = models.ForeignKey(Book, on_delete=models.DO_NOTHING, related_name='books_users')
    count = models.PositiveIntegerField(default=1)
    date = models.DateField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.book.author.count += int(self.count)
        self.book.author.save()
        self.book.count += int(self.count)
        self.book.save()
        super().save(*args, **kwargs)

