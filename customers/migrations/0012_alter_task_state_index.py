# Generated by Django 3.2.7 on 2021-10-03 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0011_task_state_index'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='state_index',
            field=models.IntegerField(),
        ),
    ]
