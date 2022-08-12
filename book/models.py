from django.db import models

# Create your models here.



class Author(models.Model):
    name = models.CharField(max_length=255, default='')
    biography = models.CharField(max_length=255, default='')
    email = models.CharField(max_length=255, default='')
    address = models.CharField(max_length=255, default='')
    def __str__(self):
        return self.name

class Publisher(models.Model):
    name = models.CharField(max_length=255, default='')
    address = models.CharField(max_length=255, default='')
    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255, default='')
    def __str__(self):
        return self.name

class Book(models.Model):
    ISBN = models.CharField(max_length=255, default='')
    title = models.CharField(max_length=255, default='')
    language = models.CharField(max_length=255, default='')
    publicationDate = models.DateTimeField()
    numberOfPage = models.IntegerField(default=0)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.title


class BookItem(models.Model):
    book = models.OneToOneField(Book, on_delete=models.SET_NULL, null=True)
    discount = models.FloatField(default=0)
    barcode = models.CharField(max_length=255, default='')
    price = models.FloatField(default=0)
    description = models.TextField(default='')
    hearder = models.CharField(max_length=255, default='')
    isPay = models.BooleanField(default=False)
    def __str__(self):
        return self.hearder


class BookItemImg(models.Model):
    bookItem = models.ForeignKey(BookItem, on_delete=models.CASCADE)
    image = models.ImageField(null=True, upload_to="book/")









