from django.db import models


# Create your models here.

class Book(models.Model):
    bookName = models.CharField(max_length=100)
    bookAuthor = models.CharField(max_length=100) 
    bookPrice = models.IntegerField()
    


class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

