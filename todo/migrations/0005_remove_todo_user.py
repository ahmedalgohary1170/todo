# Generated by Django 5.0.6 on 2024-05-17 11:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_remove_todo_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='user',
        ),
    ]