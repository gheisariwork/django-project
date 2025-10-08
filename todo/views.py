from django.shortcuts import render
from django.http import HttpResponse
from todo.models import Task


def len2(text):
    return len(text)


def home_view(request):
    list_tasks = Task.objects.all()
    titles = []
    for obj in list_tasks:
        length = len2(obj.title)
        titles.append(str(length))
    new = ", ".join(titles)
    return HttpResponse(new)


def home_view2(request):
    context = {"student": ["Ali", "hosein"]}
    return render(request, 'todo/new.html', context)


def task_view(request):
    tasks = list(Task.objects.all())
    context = {"list_tasks": tasks}
    return render(request, 'todo/start.html', context)


def task_view2(request):
    tasks = Task.objects.all()
    titles = []
    for obj in tasks:
        titles.append(obj.title)
    context = {"tasks_titles": titles}
    return render(request, 'todo/start.html', context)
