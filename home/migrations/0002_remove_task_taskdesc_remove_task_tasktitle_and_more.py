# Generated by Django 4.2.7 on 2023-12-03 07:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='taskDesc',
        ),
        migrations.RemoveField(
            model_name='task',
            name='taskTitle',
        ),
        migrations.RemoveField(
            model_name='task',
            name='time',
        ),
    ]
