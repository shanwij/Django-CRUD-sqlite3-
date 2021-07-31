from django.db import models

class book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    height = models.IntegerField()
    publisher = models.CharField(max_length=100)