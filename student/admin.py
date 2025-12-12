from django.contrib import admin
from student.models import Student, Course, Profile, Teacher

class CourseAdmin(admin.ModelAdmin):
    list_display = ("title", "code", "start_date", "teacher")
    list_filter = ("start_date", )

admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Course, CourseAdmin)
admin.site.register(Profile)
