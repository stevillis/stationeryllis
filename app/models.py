"""Models related definitions."""

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models import CheckConstraint, Q


class DayOfTheWeek(models.Model):
    """DayOfTheWeek Model."""
    description = models.CharField(
        verbose_name="Dia da Semana",
        max_length=15,
        null=False,
        blank=False,
        unique=True
    )

    class Meta:
        """Meta definitions."""
        verbose_name = "Dia da semana"
        verbose_name_plural = "Dias da semana"
        ordering = ('id', )

    def __str__(self) -> str:
        return str(self.description)


class CommissionParam(models.Model):
    """CommissionParam Model."""
    min_percentage = models.DecimalField(
        verbose_name="Percentual mínimo",
        max_digits=5,
        decimal_places=2,
        null=False,
        blank=False,
        default=3,
        validators=[
            MinValueValidator(0.0),
            MaxValueValidator(10.0)
        ]
    )
    max_percentage = models.DecimalField(
        verbose_name="Percentual máximo",
        max_digits=5,
        decimal_places=2,
        null=False,
        blank=False,
        default=5,
        validators=[
            MinValueValidator(0.0),
            MaxValueValidator(10.0)
        ]
    )
    day_of_the_week = models.OneToOneField(
        DayOfTheWeek,
        verbose_name="Dia da semana",
        on_delete=models.CASCADE,
    )

    class Meta:
        """Meta definitions."""
        verbose_name = "Parâmetro de Comissão"
        verbose_name_plural = "Parâmetros de Comissão"
        ordering = ('id', )
        constraints = (
            CheckConstraint(
                check=Q(min_percentage__gte=0.0) & Q(min_percentage__lte=10.0),
                name='%(app_label)s_%(class)s_min_percentage_range'
            ),
            CheckConstraint(
                check=Q(max_percentage__gte=0.0) & Q(max_percentage__lte=10.0),
                name='%(app_label)s_%(class)s_max_percentage_range'
            )
        )

    def __str__(self) -> str:
        return str(self.day_of_the_week.description)
