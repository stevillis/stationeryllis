"""Models related definitions."""

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
