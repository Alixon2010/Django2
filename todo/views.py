from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from todo.forms import TaskForm, UserForm, ProfileForm, CustomUserChangeForm
from todo.models import Task, Profile


@login_required
def home(request):
    all_tasks = False
    if request.user.has_group('Admin'):
        all_tasks = True

    context = {
        'all_tasks': all_tasks,
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
    if request.user.has_group('Admin'):
        task = Task.objects.get(id=task_id)
    else:
        task = Task.objects.get(id=task_id, user=request.user)
    
    task.delete()
    return redirect('home')


@login_required
def edit(request, task_id):
    if request.user.has_group('Admin'):
        task_object = Task.objects.get(id=task_id)
    else:
        task_object = Task.objects.get(id=task_id, user=request.user)
    
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
    task = Task.objects.get(id=task_id, user=request.user)
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

@login_required
def profile(request):
    user = request.user
    profile = Profile.objects.filter(user=user).first()
    context = {
        'profile': profile,
        'user': user,
    }
    return render(request, 'user/profile.html')

@login_required
def change_profile(request):
    user = request.user
    profile = Profile.objects.filter(user=user).first()
    
    if request.method == 'POST':
        u_form = CustomUserChangeForm(request.POST, instance=user)
        p_form = ProfileForm(request.POST, request.FILES, instance=profile)
        if u_form.is_valid():
            u_form.save()
            return redirect('profile')
        if p_form.is_valid():
            p = p_form.save(commit=False)
            p.user = user
            p.save()
            return redirect('profile')
    else:
        u_form = CustomUserChangeForm(instance=user)
        p_form = ProfileForm(instance=profile)
        
    return render(request, 'user/profile_change.html', {'u_form': u_form, 'p_form': p_form, 'profile': profile})

def all_tasks(request):
    if request.user.has_group('Admin'):
        tasks = Task.objects.all()
    else:
        tasks = Task.objects.filter(user=request.user)
        
    context = {
        'tasks': tasks,
        'count_completed': Task.objects.filter(is_completed=True, user=request.user).count()
    }
    
    return render(request, 'todo/all_tasks.html', context)