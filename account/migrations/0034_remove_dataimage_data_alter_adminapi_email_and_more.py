# Generated by Django 4.2.7 on 2024-02-17 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0033_dataimage"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="dataimage",
            name="data",
        ),
        migrations.AlterField(
            model_name="adminapi",
            name="email",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="adminapi",
            name="name",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="adminapi",
            name="organization",
            field=models.CharField(max_length=100),
        ),
        migrations.DeleteModel(
            name="Data",
        ),
        migrations.DeleteModel(
            name="DataImage",
        ),
    ]