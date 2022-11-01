"""Customer tests module."""


from app.models import Customer
from django.db.utils import IntegrityError
from django.test import TransactionTestCase
from mixer.backend.django import mixer


class CustomerTestCase(TransactionTestCase):
    """Customer TestCase"""

    def test_create_model_with_valid_data(self):
        """Create model with valid data should work as expected."""
        customer = mixer.blend(
            Customer,
            name="Jane",
            email="jane@example.com",
            phone="11996685050"
        )

        self.assertEqual(customer.name, "Jane")
        self.assertEqual(customer.email, "jane@example.com")
        self.assertEqual(customer.phone, "11996685050")

    def test_create_model_with_invalid_data(self):
        """Create model with valid data should work as expected."""
        valid_name = "Mike Brain Phill"
        valid_email = "mikebp@gmail.com"
        valid_phone_number = "+1 206-957-2295"

        with self.subTest("Create Customer without name should raise exception."):
            with self.assertRaises(IntegrityError):
                Customer.objects.create(  # pylint: disable=no-member
                    name=None,
                    email=valid_email,
                    phone=valid_phone_number
                )

        with self.subTest("Create Customer without email should raise exception."):
            with self.assertRaises(IntegrityError):
                Customer.objects.create(  # pylint: disable=no-member
                    name=valid_name,
                    email=None,
                    phone=valid_phone_number
                )

        with self.subTest("Create Customer without email should raise exception."):
            with self.assertRaises(IntegrityError):
                Customer.objects.create(  # pylint: disable=no-member
                    name=valid_name,
                    email="another_email@bol.com",
                    phone=None
                )
