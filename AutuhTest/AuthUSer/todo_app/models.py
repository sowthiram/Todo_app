from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length = 100)
    desc = models.CharField(max_length = 100)
    task_user = models.CharField(max_length = 100)
    due_date = models.DateField()
    status = models.CharField(max_length = 100, default="pending")

    def __str__(self):
        return self.title
