# Generated by Django 4.2.6 on 2023-11-10 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0021_employee_clock_in_is_bar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee_clock_in',
            name='is_bar',
        ),
        migrations.AddField(
            model_name='role',
            name='is_bar',
            field=models.BooleanField(default=False),
        ),
    ]
