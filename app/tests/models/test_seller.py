"""Seller tests module."""


from app.models import Seller
from django.db.utils import IntegrityError
from django.test import TransactionTestCase
from mixer.backend.django import mixer


class SellerTestCase(TransactionTestCase):
    """Seller TestCase"""

    def test_create_model_with_valid_data(self):
        """Create model with valid data should work as expected."""
        seller = mixer.blend(
            Seller,
            name="Jane",
            email="jane@example.com",
            phone="11996685050"
        )

        self.assertEqual(seller.name, "Jane")
        self.assertEqual(seller.email, "jane@example.com")
        self.assertEqual(seller.phone, "11996685050")

    def test_create_model_with_invalid_data(self):
        """Create model with valid data should work as expected."""
        valid_name = "Mike Brain Phill"
        valid_email = "mikebp@gmail.com"
        valid_phone_number = "+1 206-957-2295"

        with self.subTest("Create Seller without name should raise exception."):
            with self.assertRaises(IntegrityError):
                Seller.objects.create(  # pylint: disable=no-member
                    name=None,
                    email=valid_email,
                    phone=valid_phone_number
                )

        with self.subTest("Create Seller without email should raise exception."):
            with self.assertRaises(IntegrityError):
                Seller.objects.create(  # pylint: disable=no-member
                    name=valid_name,
                    email=None,
                    phone=valid_phone_number
                )

        with self.subTest("Create Seller without email should raise exception."):
            with self.assertRaises(IntegrityError):
                Seller.objects.create(  # pylint: disable=no-member
                    name=valid_name,
                    email="another_email@bol.com",
                    phone=None
                )

    def test_str_method(self):
        """Test str method of Model."""
        seller = mixer.blend(Seller, name="Karen")
        self.assertEqual(str(seller), "Karen")
