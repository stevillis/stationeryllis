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
        self.customer = mixer.blend(
            Customer,
            name="Linda Bob",
            email="lindabob@amazon.com",
            phone="+1 415-387-3030"
        )

    def test_get_all_customers(self):
        """Get all customers endpoint should work as expected"""
        url = reverse('get_all_customers')
        response = self.client.get(url)
        data = response.data[0]

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(data["name"], "Linda Bob")
        self.assertEqual(data["email"], "lindabob@amazon.com")
        self.assertEqual(data["phone"], "+1 415-387-3030")
