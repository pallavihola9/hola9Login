# Generated by Django 4.2.7 on 2024-02-14 18:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0020_alter_loginprofile_email_alter_loginprofile_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="applyleaves",
            name="name",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="account.loginprofile"
            ),
        ),
    ]