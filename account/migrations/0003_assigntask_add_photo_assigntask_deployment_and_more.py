# Generated by Django 4.2.7 on 2023-11-28 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0002_adminauth_assigntask_employeelogin_employeelogin2_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="assigntask",
            name="add_photo",
            field=models.ImageField(blank=True, null=True, upload_to="task_photos/"),
        ),
        migrations.AddField(
            model_name="assigntask",
            name="deployment",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="assigntask",
            name="re_deployment",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="assigntask",
            name="re_testing",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="assigntask",
            name="task_description",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="assigntask",
            name="testing",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="assigntask",
            name="testing_bug",
            field=models.BooleanField(default=False),
        ),
    ]