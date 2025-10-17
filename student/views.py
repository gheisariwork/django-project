from django.shortcuts import render
from student.models import Student, Course


def student_view(request):
    all_students = Student.objects.filter(score__gt=15)
    context = {"students": all_students}
    html_file = "student/all_student.html"
    return render(request, html_file, context)


def courses_view(request):
    all_courses = Course.objects.all()
    context = {"courses": all_courses}
    return render(request, "student/courses.html", context)
