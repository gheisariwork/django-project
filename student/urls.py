from django.urls import path
from student.views import student_view, courses_view
from student.class_views import *

app_name = "student"

urlpatterns = [
    path("all_students/", student_view, name="student_list"),
    path("courses/", courses_view),
    path("all_students_new/", AllStudentsView.as_view(), name="student_list_new"),
    path("add-course/", AddCourseView.as_view(), name="add_course"),
    path("add-profile/", AddProfileView.as_view(), name="add_profile")
]
