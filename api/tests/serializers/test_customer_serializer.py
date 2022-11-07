"""CustomerSerializer tests module."""


from django.test import TestCase

from api.serializers.customer_serializer import CustomerSerializer
from app.models import Customer


class CustomerSerializerTestCase(TestCase):
    """CustomerSerializer TestCase"""

    def setUp(self) -> None:
        """Set up common used values."""
        self.customer_attributes = {
            "name": "John Kent",
            "email": "johnkent@gmail.com",
            "phone": "+1 415-387-2249"
        }

        self.customer = Customer.objects.create(  # pylint: disable=no-member
            **self.customer_attributes
        )
        self.serializer = CustomerSerializer(instance=self.customer)

    def test_valid_data(self):
        """Test serializer with valid data."""
        data = self.serializer.data

        with self.subTest(
            "CustomerSerializer should have the exact attributes and data as expected"
        ):
            self.assertCountEqual(
                data.keys(), ["id", "name", "email", "phone"])
            self.assertEqual(data["name"], self.customer_attributes["name"])
            self.assertEqual(data["email"], self.customer_attributes["email"])
            self.assertEqual(data["phone"], self.customer_attributes["phone"])

        with self.subTest("Test if duplicate email data raise exception"):
            serializer = CustomerSerializer(data=data)
            is_valid = serializer.is_valid()

            email_errors = serializer.errors["email"]
            error_code = email_errors[0].code

            self.assertFalse(is_valid)
            self.assertCountEqual(serializer.errors, ["email"])
            self.assertEqual(error_code, "unique")

    def test_invalid_data(self):
        """Test invalid data."""
        serializer_data = {
            "name": "Mary Wayne",
            "email": "marywayne@gmail.com",
            "phone": "0800 720 5356"
        }
        with self.subTest("Test name field content with invalid data."):
            data = serializer_data.copy()
            invalid_names = [
                list((1, 2, 3)),
                dict({"invalid": "name"}),
                set([2, 4, 6])
            ]

            for invalid_name in invalid_names:
                data["name"] = invalid_name

                serializer = CustomerSerializer(data=data)

                self.assertFalse(serializer.is_valid())
                self.assertCountEqual(serializer.errors, ["name"])

        with self.subTest("Test email field content with invalid data."):
            data = serializer_data.copy()
            invalid_emails = [
                list((1, 2, 3)),
                dict({"invalid": "email"}),
                set([2, 4, 6])
            ]

            for invalid_email in invalid_emails:
                data["email"] = invalid_email

                serializer = CustomerSerializer(data=data)

                self.assertFalse(serializer.is_valid())
                self.assertCountEqual(serializer.errors, ["email"])

        with self.subTest("Test phone field content with invalid data."):
            data = serializer_data.copy()
            invalid_phones = [
                list((1, 2, 3)),
                dict({"invalid": "phone"}),
                set([2, 4, 6])
            ]

            for invalid_phone in invalid_phones:
                data["phone"] = invalid_phone

                serializer = CustomerSerializer(data=data)

                self.assertFalse(serializer.is_valid())
                self.assertCountEqual(serializer.errors, ["phone"])
