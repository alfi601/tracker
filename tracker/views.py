from django.shortcuts import render
from .models import Task  # импортируем модель задачи

def task_list(request):
    tasks = Task.objects.all()  # берём все задачи из базы
    return render(request, 'tracker/index.html', {'tasks': tasks})


def register(request):
    return render(request, 'tracker/register.html')