from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from datetime import timezone


class Book(models.Model):
    title = models.TextField()
    author = models.TextField()
    published = models.DateField()
    genre = models.TextField()
    in_stock = models.BooleanField()
    description = models.TextField()


# class User(models.Model):
#     id = models.AutoField(primary_key=True)
#     username = models.TextField()

# Imported User so no need to create a model.


class Transaction(models.Model):
    datetime = models.DateTimeField(default=timezone)
    action = models.TextField()
    book = models.ForeignKey(Book, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
