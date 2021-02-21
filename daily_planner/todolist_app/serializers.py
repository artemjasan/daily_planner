from rest_framework import serializers
from .models import Task, Category


class TasksSeralizer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    category = TasksSeralizer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = "__all__"
