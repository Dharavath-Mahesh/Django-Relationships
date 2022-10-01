from django.db import models

# Create your models here.
#book can be written by multiple authors and an author can write multiple books

class Author(models.Model): #an author can write multiple books
    author_name = models.CharField(max_length = 100)
    

    def __str__(self):
        return self.author_name
  
class Book(models.Model): #book can be written by multiple authors
    book_title = models.CharField(max_length = 100)
    desc = models.TextField(max_length = 300)
    authors = models.ManyToManyField(Author)

    def __str__(self):
        return self.book_title

    def written_by(self):
        return   ",".join([str(p) for p in self.authors.all() ])