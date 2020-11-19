from django.contrib import admin

from managebook.models import User, Book, Author, SoldBooks

admin.site.register(User)
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(SoldBooks)

