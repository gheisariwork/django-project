from django.urls import path
from student.views import student_view, courses_view

urlpatterns = [
    path("all_students/", student_view),
    path("courses/", courses_view),
]
