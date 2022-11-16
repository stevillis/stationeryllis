"""Product tests module."""


from decimal import Decimal

from django.db.utils import IntegrityError
from django.test import TransactionTestCase
from mixer.backend.django import mixer

from app.models import Product


class ProductTestCase(TransactionTestCase):
    """Product TestCase"""

    def test_create_model_with_valid_data(self):
        """Create model with valid data should work as expected."""
        product = mixer.blend(
            Product,
            description="Bolacha de Água e Sal",
            unit_price=Decimal(2.6),
            commission_percentage=Decimal(2.75),
        )

        self.assertEqual(product.description, "Bolacha de Água e Sal")
        self.assertEqual(product.unit_price, Decimal(2.6))
        self.assertEqual(product.commission_percentage, Decimal(2.75))

    def test_create_model_with_invalid_data(self):
        """Create model with valid data should work as expected."""
        valid_description = "Suco de manga"
        valid_unit_price = Decimal(9.85)
        valid_commission_percentage = Decimal(3.0)

        with self.subTest("Create Product without description should raise exception."):
            with self.assertRaises(IntegrityError):
                Product.objects.create(  # pylint: disable=no-member
                    description=None,
                    unit_price=valid_unit_price,
                    commission_percentage=valid_commission_percentage,
                )

        with self.subTest("Create Product without unit_price should raise exception."):
            with self.assertRaises(IntegrityError):
                Product.objects.create(  # pylint: disable=no-member
                    description=valid_description,
                    unit_price=None,
                    commission_percentage=valid_commission_percentage,
                )

        with self.subTest(
            "Create Product without commission_percentage should raise exception."
        ):
            with self.assertRaises(IntegrityError):
                Product.objects.create(  # pylint: disable=no-member
                    description=valid_description,
                    unit_price=valid_unit_price,
                    commission_percentage=None,
                )

        with self.subTest(
            "Create Product with unit_price negative should raise exception."
        ):
            with self.assertRaises(IntegrityError):
                Product.objects.create(  # pylint: disable=no-member
                    description=valid_description,
                    unit_price=-1.87,
                    commission_percentage=valid_commission_percentage,
                )

        with self.subTest(
            "Create Product with commission_percentage negative should raise exception."
        ):
            with self.assertRaises(IntegrityError):
                Product.objects.create(  # pylint: disable=no-member
                    description=valid_description,
                    unit_price=valid_unit_price,
                    commission_percentage=-2,
                )

    def test_str_method(self):
        """Test str method of Model."""
        product = mixer.blend(
            Product,
            description="Batata Frita",
            unit_price=4.45,
            commission_percentage=1,
        )
        self.assertEqual(str(product), "Batata Frita")
