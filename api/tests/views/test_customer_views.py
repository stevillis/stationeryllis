"""Customer Views tests module."""

from django.urls import reverse
from mixer.backend.django import mixer
from rest_framework import status
from rest_framework.test import APITestCase

from app.models import Customer


class CustomerViewsTestCase(APITestCase):
    """Customer Views TestCase"""

    def setUp(self) -> None:
        """Common data definitions"""
        self.customers_endpoint = reverse('customers')

    def test_get_all_customers(self):
        """Get all customers endpoint should work as expected"""
        mixer.blend(
            Customer,
            name="Linda Bob",
            email="lindabob@amazon.com",
            phone="+1 415-387-3030"
        )

        response = self.client.get(path=self.customers_endpoint)
        data = response.data[0]

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(data["name"], "Linda Bob")
        self.assertEqual(data["email"], "lindabob@amazon.com")
        self.assertEqual(data["phone"], "+1 415-387-3030")

    def test_create_customer_with_valid_data(self):
        """Create Customer with valid data should HTTP Created status code"""
        sample_customer_with_valid_data = {
            "name": "Kamila Leal",
            "email": "kamileal@gmail.com",
            "phone": "19 3615-1573"
        }

        response = self.client.post(
            path=self.customers_endpoint,
            data=sample_customer_with_valid_data
        )
        data = response.data

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(data["name"], "Kamila Leal")
        self.assertEqual(data["email"], "kamileal@gmail.com")
        self.assertEqual(data["phone"], "19 3615-1573")

    def test_create_customer_with_invalid_data(self):
        """Create Customer with invalid data should return HTTP Bad Request status code"""

        with self.subTest("Create Customer with empty name"):
            sample_customer_with_invalid_name = {
                "name": "",
                "email": "jeremysimon@gmail.com",
                "phone": "19 3615-1573"
            }
            response = self.client.post(
                path=self.customers_endpoint,
                data=sample_customer_with_invalid_name
            )

            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
            self.assertIn("name", response.data.keys())

        with self.subTest("Create Customer with empty email"):
            sample_customer_with_invalid_name = {
                "name": "Jeremy Simon",
                "email": "",
                "phone": "19 3615-1573"
            }
            response = self.client.post(
                path=self.customers_endpoint,
                data=sample_customer_with_invalid_name
            )

            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
            self.assertIn("email", response.data.keys())

        with self.subTest("Create Customer with empty name"):
            sample_customer_with_invalid_name = {
                "name": "",
                "email": "jeremysimon@gmail.com",
                "phone": "19 3615-1573"
            }
            response = self.client.post(
                path=self.customers_endpoint,
                data=sample_customer_with_invalid_name
            )

            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
            self.assertIn("name", response.data.keys())

        with self.subTest("Create Customer with empty phone"):
            sample_customer_with_invalid_name = {
                "name": "Jeremy Simon",
                "email": "jeremysimon@gmail.com",
                "phone": ""
            }
            response = self.client.post(
                path=self.customers_endpoint,
                data=sample_customer_with_invalid_name
            )

            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
            self.assertIn("phone", response.data.keys())

        with self.subTest("Create Customer with duplicated email"):
            sample_customer = {
                "name": "Jeremy Simon",
                "email": "jeremysimon@gmail.com",
                "phone": "19 3615-1573"
            }
            sample_customer_with_duplicated_email = {
                "name": "Jeremy Simon Patson",
                "email": "jeremysimon@gmail.com",
                "phone": "21 98455-6301"
            }

            self.client.post(
                path=self.customers_endpoint,
                data=sample_customer
            )
            response = self.client.post(
                path=self.customers_endpoint,
                data=sample_customer_with_duplicated_email
            )

            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
            self.assertIn("email", response.data.keys())
