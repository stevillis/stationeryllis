# Generated by Django 4.1.2 on 2022-10-30 05:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0003_alter_commissionparam_day_of_the_week"),
    ]

    operations = [
        migrations.AlterField(
            model_name="commissionparam",
            name="day_of_the_week",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                to="app.dayoftheweek",
                verbose_name="Dia da semana",
            ),
        ),
    ]
