from rest_framework import generics

from .models import Task
from .serializers import TasksSeralizer


class ListTask(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TasksSeralizer


class DetailTask(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TasksSeralizer
