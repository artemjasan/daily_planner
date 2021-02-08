from django.db import models
from django.utils import timezone

class User(models.Model):
    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)


class Category(models.Model):
    name = models.CharField(max_length=50)


class Task(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE,)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,)
    title = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)


    def __str__(self):
        return self.title
