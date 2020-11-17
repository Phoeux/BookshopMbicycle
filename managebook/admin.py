from django.contrib import admin

from managebook.models import User, Book, Author

admin.site.register(User)
admin.site.register(Book)
admin.site.register(Author)
