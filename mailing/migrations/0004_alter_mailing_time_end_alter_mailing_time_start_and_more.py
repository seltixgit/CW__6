# Generated by Django 4.2.2 on 2024-09-29 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mailing", "0003_alter_client_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="mailing",
            name="time_end",
            field=models.TimeField(
                help_text="Введите время в формате ЧЧ:ММ через  двоеточие. Начало времени отправки должно быть раньше окончания времени отправки ",
                verbose_name="окончание времени отправки",
            ),
        ),
        migrations.AlterField(
            model_name="mailing",
            name="time_start",
            field=models.TimeField(
                help_text="Введите время в формате ЧЧ:ММ через двоеточие. Начало времени отправки должно быть раньше окончания времени отправки ",
                verbose_name="начало времени отправки",
            ),
        ),
        migrations.AlterField(
            model_name="mailinglog",
            name="time_try",
            field=models.DateTimeField(
                auto_now_add=True, verbose_name="дата и время попытки"
            ),
        ),
    ]
