# Generated by Django 3.2.7 on 2021-10-11 17:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0021_rename_description_task_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={'ordering': ['company']},
        ),
    ]