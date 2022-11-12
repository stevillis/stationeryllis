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
        self.customers_list_endpoint = reverse("customers-list")

    def test_get_all_customers(self):
        """Get all customers endpoint should work as expected"""
        mixer.blend(
            Customer,
            name="Linda Bob",
            email="lindabob@amazon.com",
            phone="+1 415-387-3030"
        )

        response = self.client.get(path=self.customers_list_endpoint)
        data = response.data

        with self.subTest("Response data should be paginated"):
            self.assertIn("count", data)
            self.assertIn("next", data)
            self.assertIn("previous", data)
            self.assertIn("results", data)

        with self.subTest("Response data should be equal to the created product"):
            results = data["results"]
            result = results[0]

        with self.subTest("Response data should be equal to the created product"):
            results = data["results"]
            result = results[0]

            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(len(results), 1)
            self.assertEqual(result["name"], "Linda Bob")
            self.assertEqual(result["email"], "lindabob@amazon.com")
            self.assertEqual(result["phone"], "+1 415-387-3030")

    def test_create_customer_with_valid_data(self):
        """Create Customer with valid data should return HTTP Created status code"""
        sample_customer_with_valid_data = {
            "name": "Kamila Leal",
            "email": "kamileal@gmail.com",
            "phone": "19 3615-1573"
        }

        response = self.client.post(
            path=self.customers_list_endpoint,
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
                path=self.customers_list_endpoint,
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
                path=self.customers_list_endpoint,
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
                path=self.customers_list_endpoint,
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
                path=self.customers_list_endpoint,
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
                path=self.customers_list_endpoint,
                data=sample_customer
            )
            response = self.client.post(
                path=self.customers_list_endpoint,
                data=sample_customer_with_duplicated_email
            )

            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
            self.assertIn("email", response.data.keys())

    def test_get_customer_by_pk(self):
        """Test get Customer by pk endpoint"""
        new_customer = mixer.blend(
            Customer,
            name="Danger Bob",
            email="danger_bob@gmail.com",
            phone="+1 415-387-3054"
        )
        customers_detail_endpoint = reverse(
            viewname="customers-detail",
            kwargs={"pk": new_customer.pk}
        )

        response = self.client.get(customers_detail_endpoint)
        data = response.data

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data["name"], "Danger Bob")
        self.assertEqual(data["email"], "danger_bob@gmail.com")
        self.assertEqual(data["phone"], "+1 415-387-3054")

    def test_get_non_existing_customer_by_pk(self):
        """Get a non existing Customer should return HTTP Not Found status code"""
        non_existing_customer_endpoint = reverse(
            viewname="customers-detail",
            kwargs={"pk": 99999999}
        )

        response = self.client.get(non_existing_customer_endpoint)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_customer_with_valid_data(self):
        """Test update Customer endpoint with valid data"""
        customer = mixer.blend(
            Customer,
            name="Bafabon",
            email="bafabon@gmail.com",
            phone="99 99654-8521"
        )
        customers_detail_endpoint = reverse(
            viewname="customers-detail",
            kwargs={"pk": customer.pk}
        )
        customer_updated_data = {
            "name": "Linda",
            "email": "linda@gmail.com",
            "phone": "99 99654-8521"
        }

        response = self.client.put(
            path=customers_detail_endpoint,
            data=customer_updated_data
        )
        data = response.data

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data["name"], "Linda")
        self.assertEqual(data["email"], "linda@gmail.com")
        self.assertEqual(data["phone"], "99 99654-8521")

    def test_update_customer_with_invalid_data(self):
        """Update Customer with invalid data should return HTTP Bad Request status code"""
        customer = mixer.blend(
            Customer,
            name="Colonel",
            email="colonel@gmail.com",
            phone="11 3624-2400"
        )
        customers_detail_endpoint = reverse(
            viewname="customers-detail",
            kwargs={"pk": customer.pk}
        )

        with self.subTest("Update Customer with empty name"):
            customer_updated_data_with_empty_name = {
                "name": "",
                "email": "linda@gmail.com",
                "phone": "99 99654-8521"
            }
            response = self.client.put(
                path=customers_detail_endpoint,
                data=customer_updated_data_with_empty_name
            )

            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
            self.assertIn("name", response.data.keys())

        with self.subTest("Update Customer with empty email"):
            customer_updated_data_with_empty_email = {
                "name": "Linda",
                "email": "",
                "phone": "99 99654-8521"
            }
            response = self.client.put(
                path=customers_detail_endpoint,
                data=customer_updated_data_with_empty_email
            )

            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
            self.assertIn("email", response.data.keys())

        with self.subTest("Create Customer with empty phone"):
            customer_updated_data_with_empty_phone = {
                "name": "Linda",
                "email": "linda@gmail.com",
                "phone": ""
            }
            response = self.client.put(
                path=customers_detail_endpoint,
                data=customer_updated_data_with_empty_phone
            )

            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
            self.assertIn("phone", response.data.keys())

        with self.subTest("Update Customer with duplicated email"):
            mixer.blend(
                Customer,
                name="Nyang",
                email="nyang@gmail.com",
                phone="123"
            )
            customer_updated_data_with_duplicated_email = {
                "name": "Linda",
                "email": "nyang@gmail.com",
                "phone": "99 99654-8521"
            }
            response = self.client.put(
                path=customers_detail_endpoint,
                data=customer_updated_data_with_duplicated_email
            )

            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
            self.assertIn("email", response.data.keys())

    def test_update_non_existing_customer(self):
        """Update a non existing Customer should return HTTP Not Found status code"""
        non_existing_customer_endpoint = reverse(
            viewname="customers-detail",
            kwargs={"pk": 99999999}
        )
        customer_data = {
            "name": "Lorem",
            "email": "ipsum@gmail.com",
            "phone": "123456"
        }

        response = self.client.put(
            path=non_existing_customer_endpoint,
            data=customer_data
        )

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_customer(self):
        """Test delete Customer endpoint"""
        customer = mixer.blend(
            Customer,
            name="Jane Foster",
            email="fosterjane@gmail.com",
            phone="1"
        )
        customers_detail_endpoint = reverse(
            viewname="customers-detail",
            kwargs={"pk": customer.pk}
        )

        with self.subTest("Delete existing Customer should return HTTP No Content status code"):
            response = self.client.delete(customers_detail_endpoint)

            self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        with self.subTest("Delete non existing Customer should return HTTP Not Found status code"):
            response = self.client.delete(customers_detail_endpoint)

            self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
