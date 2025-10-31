from django.shortcuts import render
from django.http import HttpResponse
from todo.models import Task
from student.models import Student, Course
from django.views import View

def task_view(request):
    if request.method == "GET":
        tasks = list(Task.objects.all())
        context = {"list_tasks": tasks}
        return render(request, 'todo/start.html', context)


def task_student(request, st_id):

    tasks_student = Task.objects.filter(student_id=st_id)
    context = {"tasks": tasks_student}
    return render(request, "todo/list_student_1.html", context)
