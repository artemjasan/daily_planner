from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class Task(models.Model):
    class TaskCategories(models.TextChoices):
        GENERAL = "General", _('General')
        HOLIDAYS = "Holidays", _('Holidays')
        FOOD = "Food", _('Food')
        CAR = "CAR", _('CAR')
        LIVING = "Living", _('Living')
        HOBBIES = "Hobbies", _('Hobbies')
        SHOPPING = "Shopping", _('Shopping')
        EDUCATION = "Education", _('Education')
        HEALTH = "Health", _('Health')

    class TaskPriority(models.TextChoices):
        LOW = "Low", _('Low')
        NORMAL = "Normal", _('Normal')
        High = "High", _('High')

    category = models.CharField(max_length=30, choices=TaskCategories.choices, default=TaskCategories.GENERAL)
    priority = models.CharField(max_length=10, choices=TaskPriority.choices, default=TaskPriority.LOW)
    title = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.title
