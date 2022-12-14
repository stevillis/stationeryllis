# Generated by Django 4.1.2 on 2022-11-02 18:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0008_seller"),
    ]

    operations = [
        migrations.CreateModel(
            name="Product",
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
                (
                    "description",
                    models.CharField(max_length=100, verbose_name="Descrição"),
                ),
                (
                    "unit_price",
                    models.DecimalField(
                        decimal_places=2,
                        default=3,
                        max_digits=9,
                        validators=[django.core.validators.MinValueValidator(0.0)],
                        verbose_name="Valor unitário",
                    ),
                ),
                (
                    "commission_percentage",
                    models.DecimalField(
                        decimal_places=2,
                        default=3,
                        max_digits=5,
                        validators=[django.core.validators.MinValueValidator(0.0)],
                        verbose_name="Percentual de comissão",
                    ),
                ),
            ],
            options={
                "verbose_name": "Produto",
                "verbose_name_plural": "Produtos",
                "ordering": ("id",),
            },
        ),
        migrations.AddConstraint(
            model_name="product",
            constraint=models.CheckConstraint(
                check=models.Q(("unit_price__gte", 0.0)),
                name="app_product_min_unit_price",
            ),
        ),
        migrations.AddConstraint(
            model_name="product",
            constraint=models.CheckConstraint(
                check=models.Q(("commission_percentage__gte", 0.0)),
                name="app_product_min_commission_percentage",
            ),
        ),
    ]
