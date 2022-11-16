"""ProductSerializer tests module."""


from decimal import Decimal

from django.test import TestCase

from api.serializers.product_serializer import ProductSerializer
from app.models import Product


class ProductSerializerTestCase(TestCase):
    """ProductSerializer TestCase"""

    def setUp(self) -> None:
        """Set up common used values."""
        self.product_attributes = {
            "description": "Detergente",
            "unit_price": 2.19,
            "commission_percentage": 1.5,
        }
        self.decimal_places = 2

        self.product = Product.objects.create(
            **self.product_attributes
        )  # pylint: disable=no-member
        self.serializer = ProductSerializer(instance=self.product)

    def test_valid_data(self):
        """ProductSerializer should have the exact attributes and data as expected."""
        data = self.serializer.data

        self.assertCountEqual(
            data.keys(),
            ["id", "description", "unit_price", "commission_percentage", "endpoints"],
        )
        self.assertEqual(data["description"], self.product_attributes["description"])
        self.assertEqual(
            round(Decimal(data["unit_price"]), 2),
            round(Decimal(self.product_attributes["unit_price"]), 2),
        )
        self.assertEqual(
            round(Decimal(data["commission_percentage"]), 2),
            round(Decimal(self.product_attributes["commission_percentage"]), 2),
        )

    def test_invalid_data(self):
        """Test invalid data."""
        serializer_data = {
            "description": "Goiaba",
            "unit_price": 23.59,
            "commission_percentage": 0,
        }
        with self.subTest("Test description field content with invalid data."):
            data = serializer_data.copy()
            invalid_names = [
                list((1, 2, 3)),
                dict({"invalid": "description"}),
                set([2, 4, 6]),
            ]

            for invalid_name in invalid_names:
                data["description"] = invalid_name

                serializer = ProductSerializer(data=data)

                self.assertFalse(serializer.is_valid())
                self.assertCountEqual(serializer.errors, ["description"])

        with self.subTest("Test unit_price field content with invalid data."):
            data = serializer_data.copy()
            invalid_unit_prices = [
                list((1, 2, 3)),
                dict({"invalid": "unit_price"}),
                set([2, 4, 6]),
            ]

            for invalid_unit_price in invalid_unit_prices:
                data["unit_price"] = invalid_unit_price

                serializer = ProductSerializer(data=data)

                self.assertFalse(serializer.is_valid())
                self.assertCountEqual(serializer.errors, ["unit_price"])

        with self.subTest(
            "Test commission_percentage field content with invalid data."
        ):
            data = serializer_data.copy()
            invalid_commission_percentages = [
                list((1, 2, 3)),
                dict({"invalid": "commission_percentage"}),
                set([2, 4, 6]),
            ]

            for invalid_commission_percentage in invalid_commission_percentages:
                data["commission_percentage"] = invalid_commission_percentage

                serializer = ProductSerializer(data=data)

                self.assertFalse(serializer.is_valid())
                self.assertCountEqual(serializer.errors, ["commission_percentage"])

        with self.subTest("Negative unit_price shouldn't be valid."):
            data = serializer_data.copy()
            data["unit_price"] = -1.25

            serializer = ProductSerializer(data=data)
            is_valid = serializer.is_valid()

            self.assertFalse(is_valid)
            self.assertCountEqual(serializer.errors, ["unit_price"])

        with self.subTest("Negative commission_percentage shouldn't be valid."):
            data = serializer_data.copy()
            data["commission_percentage"] = -1.25

            serializer = ProductSerializer(data=data)
            is_valid = serializer.is_valid()

            self.assertFalse(is_valid)
            self.assertCountEqual(serializer.errors, ["commission_percentage"])
