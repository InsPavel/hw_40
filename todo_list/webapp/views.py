from django.shortcuts import render, redirect, get_object_or_404
from webapp.models import Task


def index_view(request):
    return render(request, 'index.html', context={
        'tasks': Task.objects.all()
    })

def create_view(request):
    task = Task.objects.create(
        name = request.POST.get('task_name')
    )
    return redirect('task_index')

def delete_view(request, task_pk):
    task = get_object_or_404(Task, pk=task_pk)

    if request.method == 'GET':
        return render(request, 'delete.html', context={
            'task': task
        })
    elif request.method == 'POST':
        if request.POST.get('delete') == 'yes':
            task.delete()
        return redirect('task_index')

def complete_task_view(request, task_pk):
    task = get_object_or_404(Task, pk=task_pk)
    task.status = 'done'
    task.save()
    return redirect('task_index')

def edit_task_view(request, task_pk):
    task = get_object_or_404(Task, pk=task_pk)
    if request.method == 'GET':
        context = {
            'task': task
        }
        return render(request, 'update.html', context)
    elif request.method == 'POST':
        task.name = request.POST.get('name')
        task.status = request.POST.get('status')
        task.save()

        return redirect('task_index')

def delete_all_done_view(request):
    Task.objects.filter(status='done').delete()

    return redirect('task_index')


