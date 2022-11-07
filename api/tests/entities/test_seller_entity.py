"""SellerEntity tests module."""


from django.test import TestCase

from api.entities.seller_entity import SellerEntity


class SellerEntityTestCase(TestCase):
    """SellerEntity TestCase"""

    def setUp(self) -> None:
        self.seller_entity = SellerEntity(
            name="Ana",
            email="ana@gmail.com",
            phone="(11) 98475-1515"
        )

    def test_get_properties(self):
        """SellerEntity instance should return its properties as expected"""
        self.assertEqual(self.seller_entity.name, "Ana")
        self.assertEqual(self.seller_entity.email, "ana@gmail.com")
        self.assertEqual(self.seller_entity.phone, "(11) 98475-1515")

    def test_set_properties(self):
        """SellerEntity instance should allow setting its properties as expected"""

        with self.subTest("Set name should work as expected"):
            self.seller_entity.name = "Naomi"
            self.assertEqual(self.seller_entity.name, "Naomi")

        with self.subTest("Set email should work as expected"):
            self.seller_entity.email = "naomi@gmail.com"
            self.assertEqual(self.seller_entity.email, "naomi@gmail.com")

        with self.subTest("Set phone should work as expected"):
            self.seller_entity.phone = "89 3651-4052"
            self.assertEqual(self.seller_entity.phone, "89 3651-4052")
