from django.urls import path
from todo.views import *

app_name = "todo"

urlpatterns = [
    path("home/", task_view, name="home"),
    path("task_student/<int:st_id>/", task_student),
]
