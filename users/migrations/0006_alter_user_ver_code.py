# Generated by Django 4.2.2 on 2024-09-26 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0005_alter_user_ver_code"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="ver_code",
            field=models.CharField(
                default="445330101637", max_length=15, verbose_name="код из письма"
            ),
        ),
    ]
