# Generated by Django 4.2.7 on 2024-03-08 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0042_projectdetails'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectdetails',
            name='logo',
            field=models.ImageField(upload_to='project_logo/'),
        ),
    ]
