from django.urls import path
from student.views import student_view, courses_view
from student.class_views import AllStudentsView

app_name = "student"

urlpatterns = [
    path("all_students/", student_view, name="student_list"),
    path("courses/", courses_view),
    path("all_students_new", AllStudentsView.as_view(), name="student_list_new")
]
