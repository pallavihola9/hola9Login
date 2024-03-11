# Generated by Django 4.2.7 on 2024-02-17 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0029_holiday"),
    ]

    operations = [
        migrations.CreateModel(
            name="Image3",
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
                ("image", models.ImageField(upload_to="images/")),
            ],
        ),
        migrations.AlterField(
            model_name="wantedapi2",
            name="images",
            field=models.ManyToManyField(to="account.image2"),
        ),
        migrations.CreateModel(
            name="AdminApi",
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
                ("name", models.CharField(max_length=100, unique=True)),
                ("organization", models.CharField(max_length=100, unique=True)),
                ("logo", models.ImageField(upload_to="logos/")),
                ("company_type", models.CharField(max_length=100)),
                ("company_since", models.CharField(max_length=100)),
                ("color", models.CharField(max_length=50)),
                ("company_address", models.TextField()),
                ("social_media_links", models.JSONField(default=dict)),
                ("about", models.TextField()),
                ("tagline", models.CharField(max_length=255)),
                ("no_of_employees", models.PositiveIntegerField(default=0)),
                ("domain", models.CharField(max_length=100)),
                ("user_id", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("password", models.CharField(max_length=100)),
                ("upload_images", models.ManyToManyField(to="account.image3")),
            ],
        ),
    ]
