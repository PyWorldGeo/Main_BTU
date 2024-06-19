from django.contrib import admin

# Register your models here.
from .models import Book, User, Author

admin.site.register(Book)
admin.site.register(User)
admin.site.register(Author)