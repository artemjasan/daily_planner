from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Task
from .forms import TaskForm


'''
def index(request):
    form = TaskForm()
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()  # add to the DB
            return redirect("index")  # update page
    tasks = Task.objects.all().order_by("-created")
    return render(request,
                  'todolist_app/todolist_app.html',
                  {"form": form, "tasks": tasks}
                 )


def delete_task(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return redirect("index")


def mark_complete(request, pk):
    task = Task.objects.get(id=pk)
    task.completed = True
    task.save()
    return redirect("index")


def mark_incomplete(request, pk):
    task = Task.objects.get(id=pk)
    task.completed = False
    task.save()
    return redirect("index")


def edit_task(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("index")
    return render(request, 'todolist_app/edit_task.html', {"edit_task_form": form})
'''