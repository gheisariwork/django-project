from django.shortcuts import render
from student.models import Student


def student_view(request):
    all_students = Student.objects.filter(score__gt=15)
    context = {"students": all_students}
    html_file = "student/all_student.html"
    return render(request, html_file, context)
