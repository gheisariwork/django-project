from django.urls import path
from student.views import student_view, courses_view

app_name = "student"

urlpatterns = [
    path("all_students/", student_view, name="student_list"),
    path("courses/", courses_view),
]
