"""Order tests module."""


from django.db.utils import IntegrityError
from django.test import TransactionTestCase
from django.utils import timezone
from mixer.backend.django import mixer

from app.models import Customer, Order, OrderItem, Product, Seller


class OrderTestCase(TransactionTestCase):
    """Order TestCase"""

    def setUp(self) -> None:
        """Set up common used values."""
        self.valid_datetime = timezone.now()
        self.valid_customer = mixer.blend(Customer)
        self.valid_seller = mixer.blend(Seller)

    def test_create_model_with_valid_data(self):
        """Create model with valid data should work as expected."""
        customer = mixer.blend(Customer)
        seller = mixer.blend(Seller)
        order = mixer.blend(
            Order,
            datetime=self.valid_datetime,
            invoice_number="00001001",
            customer=customer,
            seller=seller,
        )
        prd1 = mixer.blend(
            Product, description="Alho", unit_price=16.25, commission_percentage=0
        )
        prd2 = mixer.blend(
            Product, description="Pimentão", unit_price=6.20, commission_percentage=0
        )

        # Associate Products to the Order
        prd_items = [
            mixer.blend(OrderItem, order=order, product=prd1, quantity=2),
            mixer.blend(OrderItem, order=order, product=prd2, quantity=1),
        ]

        self.assertEqual(order.datetime, self.valid_datetime)
        self.assertEqual(order.invoice_number, "00001001")
        self.assertEqual(order.customer, customer)
        self.assertEqual(order.seller, seller)

        self.assertQuerysetEqual(
            OrderItem.objects.filter(order=order),  # pylint: disable=no-member
            prd_items,
        )

    def test_create_model_with_invalid_data(self):
        """Create model with valid data should work as expected."""
        with self.subTest("Create Order without datetime should raise exception."):
            with self.assertRaises(IntegrityError):
                Order.objects.create(  # pylint: disable=no-member
                    datetime=None,
                    invoice_number="00001003",
                    customer=self.valid_customer,
                    seller=self.valid_seller,
                )

        with self.subTest(
            "Create Order without invoice_number should raise exception."
        ):
            with self.assertRaises(IntegrityError):
                Order.objects.create(  # pylint: disable=no-member
                    datetime=self.valid_datetime,
                    invoice_number=None,
                    customer=self.valid_customer,
                    seller=self.valid_seller,
                )

        with self.subTest("Create Order without customer should raise exception."):
            with self.assertRaises(IntegrityError):
                Order.objects.create(  # pylint: disable=no-member
                    datetime=self.valid_datetime,
                    invoice_number="00001004",
                    customer=None,
                    seller=self.valid_seller,
                )

        with self.subTest("Create Order without seller should raise exception."):
            with self.assertRaises(IntegrityError):
                Order.objects.create(  # pylint: disable=no-member
                    datetime=self.valid_datetime,
                    invoice_number="00001005",
                    customer=self.valid_customer,
                    seller=None,
                )

    def test_invoice_number_unique(self):
        """
        Test invoice_number unique constraint. Create Order with duplicate
        invoice_number should raise exception.
        """
        first_order = mixer.blend(
            Order,
            datetime=self.valid_datetime,
            invoice_number="00009999",
            customer=self.valid_customer,
            seller=self.valid_seller,
        )
        with self.assertRaises(IntegrityError):
            Order.objects.create(  # pylint: disable=no-member
                datetime=self.valid_datetime,
                invoice_number=first_order.invoice_number,
                customer=self.valid_customer,
                seller=self.valid_seller,
            )

    def test_str_method(self):
        """Test str method of Model."""
        order = mixer.blend(Order, invoice_number="00001002")
        self.assertEqual(str(order), "00001002")
