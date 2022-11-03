# Generated by Django 4.1.2 on 2022-11-01 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0007_customer"),
    ]

    operations = [
        migrations.CreateModel(
            name="Seller",
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
                "verbose_name": "Vendedor",
                "verbose_name_plural": "Vendedores",
                "ordering": ("id",),
            },
        ),
    ]
