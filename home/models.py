from django.db import models

# Create your models here.
class Task(models.Model):
    taskTitle = models.CharField(max_length=50, default='Your default title here')  # Set your default title here
    taskDesc = models.TextField(default='Your default value here')
    time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.taskTitle

