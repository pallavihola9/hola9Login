# Generated by Django 4.2.7 on 2024-02-17 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0028_image2_wantedapi2"),
    ]

    operations = [
        migrations.CreateModel(
            name="Holiday",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.CharField(max_length=255)),
                ("holidayname", models.CharField(max_length=255)),
                ("week", models.CharField(max_length=255)),
                ("image", models.ImageField(upload_to="holiday_images/")),
                ("desc", models.CharField(max_length=255)),
                ("organization", models.CharField(max_length=255)),
            ],
        ),
    ]