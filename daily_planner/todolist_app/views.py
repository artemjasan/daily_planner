from django.shortcuts import render
from django.utils import timezone
from .models import Task

def index(request):
    tasks = Task.objects.filter(date_on=timezone.now()).order_by('date')

    if request.method == "POST":
        new_task = Task(
            title=request.POST['title'],
            #category=request.POST['category'],
        )
        new_task.save()

    return render(request, 'todolist_app/todolist_app.html', {'tasks':tasks})
