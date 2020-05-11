from django.db import models
from django.urls import reverse
import uuid

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, blank=True, null=True)
    price = models.IntegerField(default=0)
    genre = models.ManyToManyField('Genre')

    def __str__(self):
        return self.title


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return self.last_name


class Genre(models.Model):
    version = models.CharField(max_length=100)
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.version
