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


class Customer(models.Model):
    """Customer Model."""
    name = models.CharField(
        verbose_name="Nome",
        max_length=100,
        null=False,
        blank=False
    )
    email = models.EmailField(
        verbose_name="E-mail",
        null=False,
        blank=False,
        unique=True
    )
    phone = models.CharField(
        verbose_name="Telefone",
        max_length=100,
        null=False,
        blank=False
    )

    class Meta:
        """Meta definitions."""
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        ordering = ('id', )

    def __str__(self) -> str:
        return str(self.name)


class Seller(models.Model):
    """Seller Model."""
    name = models.CharField(
        verbose_name="Nome",
        max_length=100,
        null=False,
        blank=False
    )
    email = models.EmailField(
        verbose_name="E-mail",
        null=False,
        blank=False,
        unique=True
    )
    phone = models.CharField(
        verbose_name="Telefone",
        max_length=100,
        null=False,
        blank=False
    )

    class Meta:
        """Meta definitions."""
        verbose_name = "Vendedor"
        verbose_name_plural = "Vendedores"
        ordering = ('id', )

    def __str__(self) -> str:
        return str(self.name)


class Product(models.Model):
    """Product Model."""
    description = models.CharField(
        verbose_name="Descrição",
        max_length=100,
        null=False,
        blank=False
    )
    unit_price = models.DecimalField(
        verbose_name="Valor unitário",
        max_digits=9,
        decimal_places=2,
        null=False,
        blank=False,
        default=3,
        validators=[
            MinValueValidator(0.0),
        ]
    )
    commission_percentage = models.DecimalField(
        verbose_name="Percentual de comissão",
        max_digits=5,
        decimal_places=2,
        null=False,
        blank=False,
        default=3,
        validators=[
            MinValueValidator(0.0),
        ]
    )

    class Meta:
        """Meta definitions."""
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"
        ordering = ('id', )
        constraints = (
            CheckConstraint(
                check=Q(unit_price__gte=0.0),
                name='%(app_label)s_%(class)s_min_unit_price'
            ),
            CheckConstraint(
                check=Q(commission_percentage__gte=0.0),
                name='%(app_label)s_%(class)s_min_commission_percentage'
            ),
        )

    def __str__(self) -> str:
        return str(self.description)
