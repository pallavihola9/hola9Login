# Generated by Django 4.2.7 on 2024-03-13 16:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0051_adminapi_password2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='adminapi',
            name='password2',
        ),
    ]