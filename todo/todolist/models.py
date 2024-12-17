from django.db import models
from django.utils import timezone

# Create your models here.

class ToDo(models.Model):

    title = models.CharField(max_length=50)
    desc = models.TextField()
    time = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=20, default='Not Completed')

    def __str__(self) -> str:
        return self.title
