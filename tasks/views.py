from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
from .forms import TaskForm

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_all_tasks')
    else:
        form = TaskForm()
    return render(request, 'add_task.html', {'form': form})

def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('view_all_tasks')
    else:
        form = TaskForm(instance=task)
    return render(request, 'edit_task.html', {'form': form, 'task': task})

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('view_all_tasks')

def view_all_tasks(request):
    tasks = Task.objects.all()
    return render(request, 'view_all_tasks.html', {'tasks': tasks})

def filter_tasks_by_priority(request, priority):
    tasks = Task.objects.filter(priority=priority)
    return render(request, 'view_all_tasks.html', {'tasks': tasks})