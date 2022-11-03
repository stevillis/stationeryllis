"""ProductItem tests module."""


from django.db.utils import IntegrityError
from django.test import TransactionTestCase
from mixer.backend.django import mixer

from app.models import Product, ProductItem


class ProductItemTestCase(TransactionTestCase):
    """ProductItem TestCase"""

    def setUp(self) -> None:
        """Set up common used values."""
        self.valid_product = mixer.blend(
            Product,
            description="Creme dental",
            unit_price=2.99,
            commission_percentage=0
        )

    def test_create_model_with_valid_data(self):
        """Create model with valid data should work as expected."""
        order_item = mixer.blend(
            ProductItem,
            product=self.valid_product,
            quantity=10
        )

        self.assertEqual(order_item.product, self.valid_product)
        self.assertEqual(order_item.quantity, 10)

    def test_create_model_with_invalid_data(self):
        """Create model with valid data should work as expected."""
        with self.subTest("Create ProductItem without product should raise exception."):
            with self.assertRaises(IntegrityError):
                ProductItem.objects.create(  # pylint: disable=no-member
                    product=None,
                    quantity=2
                )

        with self.subTest("Create ProductItem without quantity should raise exception."):
            with self.assertRaises(IntegrityError):
                ProductItem.objects.create(  # pylint: disable=no-member
                    product=self.valid_product,
                    quantity=None
                )

        with self.subTest("Create ProductItem with quantity out of range should raise exception."):
            with self.assertRaises(IntegrityError):
                ProductItem.objects.create(  # pylint: disable=no-member
                    product=self.valid_product,
                    quantity=0
                )

    def test_str_method(self):
        """Test str method of Model."""
        order_item = mixer.blend(
            ProductItem,
            product=self.valid_product,
            quantity=30
        )
        product_id = self.valid_product.id

        self.assertEqual(
            str(order_item),
            f"<ProductItem product #{product_id}, quantity=30>"
        )
