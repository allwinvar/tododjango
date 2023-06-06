from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Task
from .forms import TodoForm


def add(request):
    task1 = Task.objects.all()
    if request.method == 'POST':
        name = request.POST.get('task','')
        priority = request.POST.get('priority','')
        date = request.POST.get('date','')
        if not priority or not date:
            messages.error(request, 'Please set all fields')
            return redirect('/')
        else:
            task = Task(name=name, priority=priority, date=date)
            task.save()
    return render(request, 'home.html', {'task1': task1})


def delete(request, id):
    task = Task.objects.get(id=id)
    if request.method == 'POST':
        task.delete()
        return redirect('/')
    return render(request, 'delete.html')


def update(request, id):
    task = Task.objects.get(id=id)
    f = TodoForm(request.POST or None, instance=task)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request, 'update.html', {'f': f, 'task': task})
