from django.contrib import admin
from .models import Book, Publisher
# Register your models here.

admin.site.register(Publisher)
admin.site.register(Book)