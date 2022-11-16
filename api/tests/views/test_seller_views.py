"""Seller Views tests module."""

from django.contrib.auth.models import User
from django.urls import reverse
from mixer.backend.django import mixer
from rest_framework import status
from rest_framework.test import APITestCase

from app.models import Seller


class SellerViewsTestCase(APITestCase):
    """Seller Views TestCase"""

    def setUp(self) -> None:
        """Common data definitions"""
        self.sellers_list_endpoint = reverse("sellers-list")

        user = User.objects.create_user("username", "Pas$w0rd")
        self.client.force_authenticate(user)

    def test_get_all_sellers(self):
        """Get all sellers endpoint should work as expected"""
        mixer.blend(
            Seller,
            name="Linda Bob",
            email="lindabob@amazon.com",
            phone="+1 415-387-3030",
        )

        response = self.client.get(path=self.sellers_list_endpoint)
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
            self.assertEqual(result["name"], "Linda Bob")
            self.assertEqual(result["email"], "lindabob@amazon.com")
            self.assertEqual(result["phone"], "+1 415-387-3030")

    def test_create_seller_with_valid_data(self):
        """Create Seller with valid data should return HTTP Created status code"""
        sample_seller_with_valid_data = {
            "name": "Kamila Leal",
            "email": "kamileal@gmail.com",
            "phone": "19 3615-1573",
        }

        response = self.client.post(
            path=self.sellers_list_endpoint, data=sample_seller_with_valid_data
        )
        data = response.data

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(data["name"], "Kamila Leal")
        self.assertEqual(data["email"], "kamileal@gmail.com")
        self.assertEqual(data["phone"], "19 3615-1573")

    def test_create_seller_with_invalid_data(self):
        """Create Seller with invalid data should return HTTP Bad Request status code"""

        with self.subTest("Create Seller with empty name"):
            sample_seller_with_invalid_name = {
                "name": "",
                "email": "jeremysimon@gmail.com",
                "phone": "19 3615-1573",
            }
            response = self.client.post(
                path=self.sellers_list_endpoint, data=sample_seller_with_invalid_name
            )

            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
            self.assertIn("name", response.data.keys())

        with self.subTest("Create Seller with empty email"):
            sample_seller_with_invalid_name = {
                "name": "Jeremy Simon",
                "email": "",
                "phone": "19 3615-1573",
            }
            response = self.client.post(
                path=self.sellers_list_endpoint, data=sample_seller_with_invalid_name
            )

            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
            self.assertIn("email", response.data.keys())

        with self.subTest("Create Seller with empty name"):
            sample_seller_with_invalid_name = {
                "name": "",
                "email": "jeremysimon@gmail.com",
                "phone": "19 3615-1573",
            }
            response = self.client.post(
                path=self.sellers_list_endpoint, data=sample_seller_with_invalid_name
            )

            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
            self.assertIn("name", response.data.keys())

        with self.subTest("Create Seller with empty phone"):
            sample_seller_with_invalid_name = {
                "name": "Jeremy Simon",
                "email": "jeremysimon@gmail.com",
                "phone": "",
            }
            response = self.client.post(
                path=self.sellers_list_endpoint, data=sample_seller_with_invalid_name
            )

            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
            self.assertIn("phone", response.data.keys())

        with self.subTest("Create Seller with duplicated email"):
            sample_seller = {
                "name": "Jeremy Simon",
                "email": "jeremysimon@gmail.com",
                "phone": "19 3615-1573",
            }
            sample_seller_with_duplicated_email = {
                "name": "Jeremy Simon Patson",
                "email": "jeremysimon@gmail.com",
                "phone": "21 98455-6301",
            }

            self.client.post(path=self.sellers_list_endpoint, data=sample_seller)
            response = self.client.post(
                path=self.sellers_list_endpoint,
                data=sample_seller_with_duplicated_email,
            )

            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
            self.assertIn("email", response.data.keys())

    def test_get_seller_by_pk(self):
        """Test get Seller by pk endpoint"""
        new_seller = mixer.blend(
            Seller,
            name="Danger Bob",
            email="danger_bob@gmail.com",
            phone="+1 415-387-3054",
        )
        sellers_detail_endpoint = reverse(
            viewname="sellers-detail", kwargs={"pk": new_seller.pk}
        )

        response = self.client.get(sellers_detail_endpoint)
        data = response.data

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data["name"], "Danger Bob")
        self.assertEqual(data["email"], "danger_bob@gmail.com")
        self.assertEqual(data["phone"], "+1 415-387-3054")

    def test_get_non_existing_seller_by_pk(self):
        """Get a non existing Seller should return HTTP Not Found status code"""
        non_existing_seller_endpoint = reverse(
            viewname="sellers-detail", kwargs={"pk": 99999999}
        )

        response = self.client.get(non_existing_seller_endpoint)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_seller_with_valid_data(self):
        """Test update Seller endpoint with valid data"""
        seller = mixer.blend(
            Seller, name="Bafabon", email="bafabon@gmail.com", phone="99 99654-8521"
        )
        sellers_detail_endpoint = reverse(
            viewname="sellers-detail", kwargs={"pk": seller.pk}
        )
        seller_updated_data = {
            "name": "Linda",
            "email": "linda@gmail.com",
            "phone": "99 99654-8521",
        }

        response = self.client.put(
            path=sellers_detail_endpoint, data=seller_updated_data
        )
        data = response.data

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data["name"], "Linda")
        self.assertEqual(data["email"], "linda@gmail.com")
        self.assertEqual(data["phone"], "99 99654-8521")

    def test_update_seller_with_invalid_data(self):
        """Update Seller with invalid data should return HTTP Bad Request status code"""
        seller = mixer.blend(
            Seller, name="Colonel", email="colonel@gmail.com", phone="11 3624-2400"
        )
        sellers_detail_endpoint = reverse(
            viewname="sellers-detail", kwargs={"pk": seller.pk}
        )

        with self.subTest("Update Seller with empty name"):
            seller_updated_data_with_empty_name = {
                "name": "",
                "email": "linda@gmail.com",
                "phone": "99 99654-8521",
            }
            response = self.client.put(
                path=sellers_detail_endpoint, data=seller_updated_data_with_empty_name
            )

            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
            self.assertIn("name", response.data.keys())

        with self.subTest("Update Seller with empty email"):
            seller_updated_data_with_empty_email = {
                "name": "Linda",
                "email": "",
                "phone": "99 99654-8521",
            }
            response = self.client.put(
                path=sellers_detail_endpoint, data=seller_updated_data_with_empty_email
            )

            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
            self.assertIn("email", response.data.keys())

        with self.subTest("Create Seller with empty phone"):
            seller_updated_data_with_empty_phone = {
                "name": "Linda",
                "email": "linda@gmail.com",
                "phone": "",
            }
            response = self.client.put(
                path=sellers_detail_endpoint, data=seller_updated_data_with_empty_phone
            )

            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
            self.assertIn("phone", response.data.keys())

        with self.subTest("Update Seller with duplicated email"):
            mixer.blend(Seller, name="Nyang", email="nyang@gmail.com", phone="123")
            seller_updated_data_with_duplicated_email = {
                "name": "Linda",
                "email": "nyang@gmail.com",
                "phone": "99 99654-8521",
            }
            response = self.client.put(
                path=sellers_detail_endpoint,
                data=seller_updated_data_with_duplicated_email,
            )

            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
            self.assertIn("email", response.data.keys())

    def test_update_non_existing_seller(self):
        """Update a non existing Seller should return HTTP Not Found status code"""
        non_existing_seller_endpoint = reverse(
            viewname="sellers-detail", kwargs={"pk": 99999999}
        )
        seller_data = {"name": "Lorem", "email": "ipsum@gmail.com", "phone": "123456"}

        response = self.client.put(path=non_existing_seller_endpoint, data=seller_data)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_seller(self):
        """Test delete Seller endpoint"""
        seller = mixer.blend(
            Seller, name="Jane Foster", email="fosterjane@gmail.com", phone="1"
        )
        sellers_detail_endpoint = reverse(
            viewname="sellers-detail", kwargs={"pk": seller.pk}
        )

        with self.subTest(
            "Delete existing Seller should return HTTP No Content status code"
        ):
            response = self.client.delete(sellers_detail_endpoint)

            self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        with self.subTest(
            "Delete non existing Seller should return HTTP Not Found status code"
        ):
            response = self.client.delete(sellers_detail_endpoint)

            self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
