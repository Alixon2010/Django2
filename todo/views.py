from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from todo.forms import TaskForm, UserForm
from todo.models import Task


@login_required
def home(request):
    context = {
        'tasks': Task.objects.filter(user=request.user),
        'count_completed': Task.objects.filter(is_completed=True, user=request.user).count()
    }

    return render(request, 'todo/home.html', context=context)


@login_required
def add(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('home')

    else:
        form = TaskForm()

    context = {
        'form': form
    }
    return render(request, 'todo/add.html', context)


@login_required
def delete(request, task_id):
    task = Task.objects.get(id=task_id)
    if request.user == task.user:
        task.delete()
    return redirect('home')


@login_required
def edit(request, task_id):
    task_object = Task.objects.get(id=task_id)
    form = TaskForm(instance=task_object)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task_object)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('home')

    return render(request, 'todo/edit.html', context={'form': form, 'task': task_object})


# def view(request, task_id):
#     return render(request, '')

@login_required
def complete(request, task_id):
    task = Task.objects.get(id=task_id)
    task.is_completed = True
    task.save()

    return redirect('home')


def register(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')

    return render(request, 'user/register.html', {'form': form})


@login_required
def log_out(request):
    logout(request)
    return redirect('home')
