from django.urls import path
from todo.views import *

urlpatterns = [
    path("home/", home_view),
    path("home2/", home_view2),
    path("home3/", task_view),
    path("home4/", task_view2),
    path("task_student/<int:st_id>/", task_student)
]
