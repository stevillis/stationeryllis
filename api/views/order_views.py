"""Order views module"""

from typing import List, Union

from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers.order_serializer import OrderSerializer
from api.services import order_item_service, order_service, product_service


def _validate_request_data_valid(data) -> Union[bool, List]:
    """
    Check if the request data has the expected format and values.

    Args:
        data: the POST request data.

    Returns:
        A tuple with a bool value indicating that the data is valid or not,
        and a dict with the found error.
    """
    errors = {"detail": []}
    if not data.get("order"):
        errors["detail"].append(
            {
                "order": "Missing `order`"
            }
        )

    if not data.get("products"):
        errors["detail"].append(
            {
                "products": "Missing `products`"
            }
        )

    for index, product in enumerate(data.get("products")):
        quantity = product.get("quantity")
        if not quantity:
            errors["detail"].append(
                {
                    "quantity": f"Missing `quantity` in `products` at index #{index}"
                }
            )

        product_id = product.get("id")
        product_service.get_product_by_pk(product_id)

        if len(errors["detail"]) > 0:
            return False, errors

    return True, []


class OrderList(APIView):
    """Non parameter dependent Views"""

    def get(self, request, format=None):
        """Get all Orders View"""
        orders = order_service.get_all_orders()

        pagination = PageNumberPagination()
        paginated_orders = pagination.paginate_queryset(orders, request)

        serializer = OrderSerializer(instance=paginated_orders, many=True)

        return pagination.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        """
        Create a Order View.

        A sample of the body expected is:
        >>> {
            "order": {
                "datetime": "2022-11-06T16:15:39.318891-04:00",
                "ivoice_number": "10001001",
                "customer": 1,
                "seller": 2
            },
            "products" [
                {
                    "id": 1,
                    "quantity": 4
                },
                {
                    "id": 2,
                    "quantity": 9
                },
            ]
        }
        """
        data = request.data
        is_request_data_valid, errors = _validate_request_data_valid(data)

        if is_request_data_valid:
            products = data["products"]
            order = data["order"]

            # Create Order
            serializer = OrderSerializer(data=order)
            if serializer.is_valid():
                order_db = serializer.save()
                order_db.refresh_from_db()

                for product in products:
                    order_item_service.create_order_item(
                        order_id=order_db.id,
                        product_id=product["id"],
                        quantity=product["quantity"]
                    )

                return Response(serializer.data, status=status.HTTP_201_CREATED)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response(errors, status=status.HTTP_400_BAD_REQUEST)


class OrderDetail(APIView):
    """Parameter dependent Views"""

    def get(self, request, pk, format=None):
        """Get a Order by pk View"""
        order = order_service.get_order_by_pk(pk)
        serializer = OrderSerializer(order)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        """Update Order data View"""
        old_order = order_service.get_order_by_pk(pk)

        data = request.data
        is_request_data_valid, errors = _validate_request_data_valid(data)

        if is_request_data_valid:
            order = data["order"]
            products = data["products"]

            serializer = OrderSerializer(
                instance=old_order,
                data=order
            )
            if serializer.is_valid():
                order_db = serializer.save()
                order_db.refresh_from_db()

                order_items = order_item_service.get_order_items_by_order(
                    order_db
                )

                # Remove product items
                for order_item in order_items:
                    if order_item not in [product["id"] for product in products]:
                        order_item_service.delete_order_item(order_item)

                # Add product items
                for product in products:
                    product_id = product["id"]
                    if product_id not in [product_id for order_item.product_id in order_items]:
                        order_item_service.create_order_item(
                            order_id=order_db.id,
                            product_id=product_id,
                            quantity=product["quantity"]
                        )

                return Response(serializer.data, status=status.HTTP_200_OK)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response(errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        """Delete Order data View"""
        order = order_service.get_order_by_pk(pk)
        order_service.delete_order(order)

        return Response(status=status.HTTP_204_NO_CONTENT)
