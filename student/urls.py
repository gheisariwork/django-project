from django.urls import path
from student.views import student_view

urlpatterns = [
    path("all/", student_view)
]
