# Generated by Django 4.2.7 on 2024-02-14 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0016_assigntask_dummyone_assigntask_postdate_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="assigntask",
            name="postdate",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
