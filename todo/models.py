from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=256)
    done = models.BooleanField(default=False)
    category = models.CharField(max_length=64)
    description = models.TextField()
    # date = models.DateField()
