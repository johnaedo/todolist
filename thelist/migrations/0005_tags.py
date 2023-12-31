# Generated by Django 4.2.5 on 2023-10-26 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thelist', '0004_tasks_duedate_tasks_priority_tasks_tag'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tagName', models.CharField(help_text='Tag name', max_length=80)),
                ('tagDescr', models.CharField(help_text='Meaning of the tag', max_length=300, null=True)),
            ],
        ),
    ]
