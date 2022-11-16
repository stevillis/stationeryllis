"""Product views module"""

from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from api.serializers.product_serializer import ProductSerializer
from api.services import product_service


class ProductList(GenericAPIView):
    """Non parameter dependent Views"""

    serializer_class = ProductSerializer

    def get(self, request, format=None):
        """Get all Products View"""
        products = product_service.get_all_products()

        pagination = PageNumberPagination()
        paginated_products = pagination.paginate_queryset(products, request)

        serializer = ProductSerializer(instance=paginated_products, many=True)

        return pagination.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        """Create a Product View"""
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductDetail(GenericAPIView):
    """Parameter dependent Views"""

    serializer_class = ProductSerializer

    def get(self, request, pk, format=None):
        """Get a Product by pk View"""
        product = product_service.get_product_by_pk(pk)
        serializer = ProductSerializer(product)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        """Update Product data View"""
        old_product = product_service.get_product_by_pk(pk)
        serializer = ProductSerializer(instance=old_product, data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        """Delete Product data View"""
        product = product_service.get_product_by_pk(pk)
        product_service.delete_product(product)

        return Response(status=status.HTTP_204_NO_CONTENT)
