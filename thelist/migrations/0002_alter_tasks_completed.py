# Generated by Django 4.2.5 on 2023-10-05 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thelist', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='completed',
            field=models.BooleanField(help_text='Is this task completed?.', null=True),
        ),
    ]
