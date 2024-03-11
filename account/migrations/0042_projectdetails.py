# Generated by Django 4.2.7 on 2024-03-08 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0041_rename_wantedapi2_multiplimages_notification'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projectname', models.CharField(blank=True, max_length=255, null=True)),
                ('logo', models.ImageField(upload_to='logo_image/')),
                ('employeename', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
