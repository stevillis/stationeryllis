"""ProductEntity tests module."""


from decimal import Decimal

from django.test import TestCase

from api.entities.product_entity import ProductEntity


class ProductEntityTestCase(TestCase):
    """ProductEntity TestCase"""

    def setUp(self) -> None:
        self.product_entity = ProductEntity(
            description="Bolacha de Água e Sal",
            unit_price=Decimal(4.45),
            commission_percentage=Decimal(1),
        )

    def test_get_properties(self):
        """ProductEntity instance should return its properties as expected"""
        self.assertEqual(self.product_entity.description, "Bolacha de Água e Sal")
        self.assertEqual(self.product_entity.unit_price, Decimal(4.45))
        self.assertEqual(self.product_entity.commission_percentage, Decimal(1))

    def test_set_properties(self):
        """ProductEntity instance should allow setting its properties as expected"""

        with self.subTest("Set description should work as expected"):
            self.product_entity.description = "Leite"
            self.assertEqual(self.product_entity.description, "Leite")

        with self.subTest("Set unit_price should work as expected"):
            self.product_entity.unit_price = Decimal(3.89)
            self.assertEqual(self.product_entity.unit_price, Decimal(3.89))

        with self.subTest("Set commission_percentage should work as expected"):
            self.product_entity.commission_percentage = Decimal(2)
            self.assertEqual(self.product_entity.commission_percentage, Decimal(2))
