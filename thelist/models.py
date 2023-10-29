from django.db import models

class Tags(models.Model):
    tagName = models.CharField(max_length=80, help_text="Tag name", null=False)
    tagDescr = models.CharField(max_length=300, help_text="Meaning of the tag", null=True)


class Tasks(models.Model):
    descr = models.CharField(max_length=300,help_text="The text of your task.")
    completed = models.BooleanField(help_text="Is this task completed?.", null=True)
    dateCompleted = models.DateField(help_text ="When the task was completed.", null=True)
    dueDate = models.DateField(help_text="When is this task due", null=True)
    tag_id = models.ForeignKey(Tags, on_delete=models.DO_NOTHING, null=True)
    priority = models.IntegerField(help_text="Priority Level", null=True)


