from django.db import models
from django.utils import timezone

# Create your models here.
class Book(models.Model):
    title = models.TextField()
    author = models.TextField()
    published = models.DateField()
    genre = models.TextField()
    in_stock = models.BooleanField()
    description = models.TextField()

    def __str__(self):
        return self.title


class Transaction(models.Model):
    datetime = models.DateTimeField(default=timezone.now)
    action = models.TextField()
    book = models.ForeignKey(Book, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.book} at {self.datetime}"