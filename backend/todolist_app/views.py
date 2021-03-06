from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Task
from .serializers import TasksSeralizer


class ListTask(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TasksSeralizer


class DetailTask(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TasksSeralizer


class CategoriesList(APIView):
    def get(self, request, format=None):
        categories_dict = dict(Task.TaskCategories.choices)
        return Response(categories_dict)


class PrioritiesList(APIView):
    def get(self, request, format=None):
        priority_dict = dict(Task.TaskPriority.choices)
        return Response(priority_dict)
