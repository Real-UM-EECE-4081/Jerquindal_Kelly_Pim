# Generated by Django 4.1.1 on 2022-11-03 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_task_complete_task_notify'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='name',
            field=models.CharField(default='', max_length=255),
        ),
    ]
