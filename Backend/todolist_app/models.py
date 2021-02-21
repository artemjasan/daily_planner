from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Task(models.Model):
    category = models.ForeignKey(Category, default="General", on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False, blank=True, null=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.title
