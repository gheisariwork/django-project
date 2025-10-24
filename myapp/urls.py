from django.contrib import admin
from django.urls import path, include
from myapp.views import index
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("todo/", include("todo.urls")),
    path("student/", include("student.urls")),
    path("account/", include("account.urls")),
    # path("", index),
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL,
                                   document_root=settings.MEDIA_ROOT)
