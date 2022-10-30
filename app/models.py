"""Models related definitions."""

from enum import unique

from django.db import models


class DayOfTheWeek(models.Model):
    """DayOfTheWeek Model."""
    description = models.CharField(
        verbose_name="Dia da Semana",
        max_length=15,
        null=False,
        blank=False,
        unique=True
    )


class CommissionParam(models.Model):
    """CommissionParam Model."""
    min_percentage = models.DecimalField(
        verbose_name="Percentual mínimo",
        max_digits=5,
        decimal_places=2,
        null=False,
        blank=False,
        default=3
    )
    max_percentage = models.DecimalField(
        verbose_name="Percentual máximo",
        max_digits=5,
        decimal_places=2,
        null=False,
        blank=False,
        default=5
    )
    day_of_the_week = models.OneToOneField(
        DayOfTheWeek,
        verbose_name="Dia da semana",
        on_delete=models.CASCADE,
    )
