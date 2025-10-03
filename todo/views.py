from django.shortcuts import render
from django.http import HttpResponse
from todo.models import Task


def len2(text):
    return len(text)


def home(request):
    list_tasks = Task.objects.all()
    titles = []
    for obj in list_tasks:
        length = len2(obj.title)
        titles.append(str(length))
    new = ", ".join(titles)
    return HttpResponse(new)
