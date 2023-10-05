# Generated by Django 4.2.4 on 2023-10-02 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Tasks",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "descr",
                    models.CharField(
                        help_text="The text of your task.", max_length=300
                    ),
                ),
                (
                    "completed",
                    models.BooleanField(help_text="Is this task completed?."),
                ),
                (
                    "dateCompleted",
                    models.DateField(help_text="When the task was completed."),
                ),
            ],
        ),
    ]