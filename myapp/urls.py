from django.contrib import admin
from django.urls import path, include
from myapp.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path("todo/", include("todo.urls")),
    path("student/", include("student.urls")),
    # path("", index),
]
