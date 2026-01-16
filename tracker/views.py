from .forms import TaskForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login
from .models import Task


def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tracker/index.html', {'tasks': tasks})


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')

        user = User.objects.create_user(
            username=username,
            email=email
        )

        user.set_unusable_password()
        user.save()

        login(request, user)

        return redirect('start')

    return render(request, 'tracker/register.html')


def start(request):
    return render(request, 'tracker/start.html')


def task_list(request):
    tasks = Task.objects.filter(user=request.user)
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('task_list')

    return render(request, 'tracker/task_list.html', {
        'tasks': tasks,
        'form': form
    })
