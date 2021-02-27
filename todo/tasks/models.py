from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Task(models.Model):
    content = models.TextField()
    date_start = models.DateTimeField(default=timezone.now)
    date_end = models.DateTimeField()
    check_done = models.BooleanField(default=False)

    def __str__(self):
        return self.content