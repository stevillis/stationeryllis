"""Product Views tests module."""

from decimal import Decimal

from django.contrib.auth.models import User
from django.urls import reverse
from mixer.backend.django import mixer
from rest_framework import status
from rest_framework.test import APITestCase

from app.models import Product


class ProductViewsTestCase(APITestCase):
    """Product Views TestCase"""

    def setUp(self) -> None:
        """Common data definitions"""
        self.products_list_endpoint = reverse("products-list")

        user = User.objects.create_user("username", "Pas$w0rd")
        self.client.force_authenticate(user)

    def test_get_all_products(self):
        """Get all products endpoint should work as expected"""
        mixer.blend(
            Product,
            description="Guaraná ralado",
            unit_price=6.85,
            commission_percentage=1.25,
        )

        response = self.client.get(path=self.products_list_endpoint)
        data = response.data

        with self.subTest("Response data should be paginated"):
            self.assertIn("count", data)
            self.assertIn("next", data)
            self.assertIn("previous", data)
            self.assertIn("results", data)

        with self.subTest("Response data should be equal to the created product"):
            results = data["results"]
            result = results[0]

            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(len(results), 1)
            self.assertEqual(result["description"], "Guaraná ralado")
            self.assertEqual(Decimal(result["unit_price"]), round(Decimal(6.85), 2))
            self.assertEqual(
                Decimal(result["commission_percentage"]), round(Decimal(1.25), 2)
            )

    def test_create_product_with_valid_data(self):
        """Create Product with valid data should return HTTP Created status code"""
        sample_product_with_valid_data = {
            "description": "Milharina",
            "unit_price": 4.95,
            "commission_percentage": 2.5,
        }

        response = self.client.post(
            path=self.products_list_endpoint, data=sample_product_with_valid_data
        )
        data = response.data

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(data["description"], "Milharina")
        self.assertEqual(Decimal(data["unit_price"]), round(Decimal(4.95), 2))
        self.assertEqual(Decimal(data["commission_percentage"]), round(Decimal(2.5), 2))

    def test_create_product_with_invalid_data(self):
        """Create Product with invalid data should return HTTP Bad Request status code"""
        with self.subTest(
            "Create Product with empty description should return Bad Request"
        ):
            sample_product_with_invalid_description = {
                "description": "",
                "unit_price": 1.99,
                "commission_percentage": 1,
            }
            response = self.client.post(
                path=self.products_list_endpoint,
                data=sample_product_with_invalid_description,
            )

            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
            self.assertIn("description", response.data.keys())

        with self.subTest(
            "Create Product with empty unit_price should return Bad Request"
        ):
            sample_product_with_invalid_unit_price = {
                "description": "Doritos",
                "unit_price": "",
                "commission_percentage": 1,
            }
            response = self.client.post(
                path=self.products_list_endpoint,
                data=sample_product_with_invalid_unit_price,
            )

            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
            self.assertIn("unit_price", response.data.keys())

        with self.subTest(
            "Create Product with negative unit_price should return Bad Request"
        ):
            sample_product_with_invalid_unit_price = {
                "description": "Doritos",
                "unit_price": -1,
                "commission_percentage": 1,
            }
            response = self.client.post(
                path=self.products_list_endpoint,
                data=sample_product_with_invalid_unit_price,
            )

            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
            self.assertIn("unit_price", response.data.keys())

        with self.subTest(
            "Create Product with empty commission_percentage should return Bad Request"
        ):
            sample_product_with_invalid_commission_percentage = {
                "description": "Doritos",
                "unit_price": 3,
                "commission_percentage": "",
            }
            response = self.client.post(
                path=self.products_list_endpoint,
                data=sample_product_with_invalid_commission_percentage,
            )

            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
            self.assertIn("commission_percentage", response.data.keys())

        with self.subTest(
            "Create Product with negative commission_percentage should return Bad Request"
        ):
            sample_product_with_invalid_commission_percentage = {
                "description": "Doritos",
                "unit_price": 3,
                "commission_percentage": -1,
            }
            response = self.client.post(
                path=self.products_list_endpoint,
                data=sample_product_with_invalid_commission_percentage,
            )

            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
            self.assertIn("commission_percentage", response.data.keys())

    def test_get_product_by_pk(self):
        """Test get Product by pk endpoint"""
        new_product = mixer.blend(
            Product, description="Potato", unit_price=4, commission_percentage=1
        )
        products_detail_endpoint = reverse(
            viewname="products-detail", kwargs={"pk": new_product.pk}
        )

        response = self.client.get(products_detail_endpoint)
        data = response.data

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data["description"], "Potato")
        self.assertEqual(round(Decimal(data["unit_price"]), 2), round(Decimal(4), 2))
        self.assertEqual(
            round(Decimal(data["commission_percentage"]), 2), round(Decimal(1), 2)
        )

    def test_get_non_existing_product_by_pk(self):
        """Get a non existing Product should return HTTP Not Found status code"""
        non_existing_product_endpoint = reverse(
            viewname="products-detail", kwargs={"pk": 99999999}
        )

        response = self.client.get(non_existing_product_endpoint)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_product_with_valid_data(self):
        """Test update Product endpoint with valid data"""
        product = mixer.blend(
            Product, description="Açaí", unit_price=2.9, commission_percentage=0
        )
        products_detail_endpoint = reverse(
            viewname="products-detail", kwargs={"pk": product.pk}
        )
        product_updated_data = {
            "description": "Cupuaçu",
            "unit_price": 46.5,
            "commission_percentage": 1,
        }

        response = self.client.put(
            path=products_detail_endpoint, data=product_updated_data
        )
        data = response.data

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data["description"], "Cupuaçu")
        self.assertEqual(Decimal(data["unit_price"]), round(Decimal(46.5), 2))
        self.assertEqual(Decimal(data["commission_percentage"]), round(Decimal(1), 2))

    def test_update_product_with_invalid_data(self):
        """Update Product with invalid data should return HTTP Bad Request status code"""
        product = mixer.blend(
            Product, description="Sabonete", unit_price=1.79, commission_percentage=1
        )
        products_detail_endpoint = reverse(
            viewname="products-detail", kwargs={"pk": product.pk}
        )

        with self.subTest("Update Product with empty description"):
            product_updated_data_with_empty_name = {
                "description": "",
                "unit_price": 2,
                "commission_percentage": 0,
            }
            response = self.client.put(
                path=products_detail_endpoint, data=product_updated_data_with_empty_name
            )

            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
            self.assertIn("description", response.data.keys())

        with self.subTest("Update Product with empty email"):
            product_updated_data_with_empty_email = {
                "description": "Sabonete líquido",
                "unit_price": "",
                "commission_percentage": 0,
            }
            response = self.client.put(
                path=products_detail_endpoint,
                data=product_updated_data_with_empty_email,
            )

            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
            self.assertIn("unit_price", response.data.keys())

        with self.subTest("Create Product with empty commission_percentage"):
            product_updated_data_with_empty_phone = {
                "description": "Sabonete líquido",
                "unit_price": 2,
                "commission_percentage": "",
            }
            response = self.client.put(
                path=products_detail_endpoint,
                data=product_updated_data_with_empty_phone,
            )

            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
            self.assertIn("commission_percentage", response.data.keys())

        with self.subTest("Update Product with negative unit_price"):
            product_updated_data_with_empty_email = {
                "description": "Sabonete líquido",
                "unit_price": -1,
                "commission_percentage": 0,
            }
            response = self.client.put(
                path=products_detail_endpoint,
                data=product_updated_data_with_empty_email,
            )

            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
            self.assertIn("unit_price", response.data.keys())

        with self.subTest("Update Product with negative commission_percentage"):
            product_updated_data_with_empty_email = {
                "description": "Sabonete líquido",
                "unit_price": 2,
                "commission_percentage": -1,
            }
            response = self.client.put(
                path=products_detail_endpoint,
                data=product_updated_data_with_empty_email,
            )

            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
            self.assertIn("commission_percentage", response.data.keys())

    def test_update_non_existing_product(self):
        """Update a non existing Product should return HTTP Not Found status code"""
        non_existing_product_endpoint = reverse(
            viewname="products-detail", kwargs={"pk": 99999999}
        )
        product_data = {
            "description": "Lorem",
            "unit_price": 10,
            "commission_percentage": 2,
        }

        response = self.client.put(
            path=non_existing_product_endpoint, data=product_data
        )

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_product(self):
        """Test delete Product endpoint"""
        product = mixer.blend(
            Product, description="Toothbrush", unit_price=2, commission_percentage=0
        )
        products_detail_endpoint = reverse(
            viewname="products-detail", kwargs={"pk": product.pk}
        )

        with self.subTest(
            "Delete existing Product should return HTTP No Content status code"
        ):
            response = self.client.delete(products_detail_endpoint)

            self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        with self.subTest(
            "Delete non existing Product should return HTTP Not Found status code"
        ):
            response = self.client.delete(products_detail_endpoint)

            self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
