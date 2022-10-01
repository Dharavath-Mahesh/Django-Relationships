from django.contrib import admin
from .models import Author, Book
# Register your models here.
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display =['author_name']


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['book_title', 'desc', 'written_by']