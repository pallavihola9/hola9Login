# Generated by Django 4.2.7 on 2024-02-17 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0034_remove_dataimage_data_alter_adminapi_email_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="adminapi",
            name="images",
            field=models.ManyToManyField(to="account.image"),
        ),
    ]
