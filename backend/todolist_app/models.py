from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class Task(models.Model):
    class TaskCategories(models.IntegerChoices):
        GENERAL = 1, _('General')
        HOLIDAYS = 2, _('Holidays')
        FOOD = 3, _('Food')
        CAR = 4, _('Car')
        LIVING = 5, _('Living')
        HOBBIES = 6, _('Hobbies')
        SHOPPING = 7, _('Shopping')
        EDUCATION = 8, _('Education')
        HEALTH = 9, _('Health')

    class TaskPriority(models.IntegerChoices):
        LOW = 1, _('Low')
        NORMAL = 2, _('Normal')
        HIGH = 3, _('High')

    category = models.PositiveSmallIntegerField(choices=TaskCategories.choices, default=TaskCategories.GENERAL)
    priority = models.PositiveSmallIntegerField(choices=TaskPriority.choices, default=TaskPriority.LOW)
    title = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.title
