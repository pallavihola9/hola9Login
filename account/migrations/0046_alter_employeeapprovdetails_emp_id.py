# Generated by Django 4.2.7 on 2024-03-08 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0045_employeeapprovdetails'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeeapprovdetails',
            name='emp_id',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
