# Generated by Django 4.1.2 on 2022-11-01 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0006_alter_commissionparam_options_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Customer",
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
                ("name", models.CharField(max_length=100, verbose_name="Nome")),
                (
                    "email",
                    models.EmailField(
                        max_length=254, unique=True, verbose_name="E-mail"
                    ),
                ),
                ("phone", models.CharField(max_length=100, verbose_name="Telefone")),
            ],
            options={
                "verbose_name": "Cliente",
                "verbose_name_plural": "Clientes",
                "ordering": ("id",),
            },
        ),
    ]
