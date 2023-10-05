from django.db import models


class Tasks(models.Model):
    descr = models.CharField(max_length=300,help_text="The text of your task.")
    completed = models.BooleanField(help_text="Is this task completed?.", null=True)
    dateCompleted = models.DateField(help_text ="When the task was completed.", null=True)

