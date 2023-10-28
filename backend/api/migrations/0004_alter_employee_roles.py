# Generated by Django 4.2.6 on 2023-10-26 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_employee_roles'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='roles',
            field=models.ManyToManyField(blank=True, related_name='employees', through='api.Employee_Role', to='api.role'),
        ),
    ]
