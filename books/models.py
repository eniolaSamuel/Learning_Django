from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.


class User(AbstractUser):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=11)


class Author(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)


class Book(models.Model):
    GENRE_CHOICES = [
        ('FICTION', 'Fiction'),
        ('FINANCE', 'Finance'),
        ('POLITICS', 'Politics'),
        ('ROMANCE', 'Romance')
    ]
    title = models.CharField(max_length=250, blank=False)
    isbn = models.CharField(max_length=13)
    genre = models.CharField(max_length=8, choices=GENRE_CHOICES, default='Finance')
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    date_published = models.DateField(blank=True, null=True)
    copies = models.IntegerField()


class Address(models.Model):
    number = models.CharField(max_length=10)
    street_name = models.CharField(max_length=250)
    city = models.CharField(max_length=250)
    state = models.CharField(max_length=250)
    country = models.CharField(max_length=100, default="Nigeria")


class BookInstance(models.Model):
    book = models.OneToOneField(Book, on_delete=models.PROTECT, primary_key=True)
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    Date_Borrowed = models.DateField(auto_now_add=True)
    Date_Returned = models.DateField()
