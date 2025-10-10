from django.db import models


class Student(models.Model):
    fullname = models.CharField(max_length=64)
    username = models.CharField(max_length=64)
    score = models.PositiveIntegerField()

    def __str__(self):
        return self.fullname
