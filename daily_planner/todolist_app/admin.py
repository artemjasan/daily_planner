from django.contrib import admin
from .models import Task, Category


class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'completed')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Task, TaskAdmin)
admin.site.register(Category, CategoryAdmin)
