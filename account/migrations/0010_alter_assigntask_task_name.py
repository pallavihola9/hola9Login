# Generated by Django 4.2.7 on 2023-12-11 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0009_employeelogin_backend_employeelogin_backend_tl_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="assigntask",
            name="task_name",
            field=models.CharField(max_length=255, null=True),
        ),
    ]
