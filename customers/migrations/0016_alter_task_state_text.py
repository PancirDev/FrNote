# Generated by Django 3.2.7 on 2021-10-03 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0015_auto_20211003_1544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='state_text',
            field=models.CharField(max_length=20),
        ),
    ]
