from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    fullname = models.CharField(max_length=64)
    score = models.PositiveIntegerField(default=0)
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)


class Teacher(models.Model):
    fullname = models.CharField(max_length=64)
    score = models.PositiveIntegerField(default=0)
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)

class Course(models.Model):
    title = models.CharField(max_length=64)
    code = models.PositiveIntegerField()
    desc = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    students = models.ManyToManyField(Student, related_name="courses")


class Profile(models.Model):
    bio = models.TextField()
    avatar = models.ImageField(upload_to="images/%Y/%m/", null=True)
    student = models.OneToOneField(Student, related_name="profile", on_delete=models.CASCADE, blank=True, null=True)
    teacher = models.OneToOneField(Teacher, related_name="profile", on_delete=models.CASCADE, blank=True, null=True)
    phone_number = models.CharField(max_length=13)
    img = models.ImageField(upload_to="images/%Y/%m/", null=True, blank=True)
    file = models.FileField(upload_to="files/%Y/%m/", null=True, blank=True)

    def __str__(self):
        return self.bio
