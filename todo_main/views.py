from django.shortcuts import render, redirect
from .models import Task


def home(request):
    # Add task
    if request.method == "POST":
        title = request.POST.get('task')
        if title:
            Task.objects.create(title=title)

    # Fetch tasks
    tasks = Task.objects.filter(is_completed=False)
    completed_tasks = Task.objects.filter(is_completed=True)

    return render(request, 'home.html', {
        'tasks': tasks,
        'completed_tasks': completed_tasks
    })


def complete_task(request, id):
    task = Task.objects.get(id=id)
    task.is_completed = True
    task.save()
    return redirect('home')


def delete_task(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    return redirect('home')