from django.shortcuts import render

def index(request):
    return render(request, 'todolist_app.html')
