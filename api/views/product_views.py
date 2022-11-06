"""Product views module"""

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.entities.product_entity import ProductEntity
from api.serializers.product_serializer import ProductSerializer
from api.services import product_service


class ProductList(APIView):
    """Non parameter dependent Views"""

    def get(self, request, format=None):
        """Get all Products View"""
        products = product_service.get_all_products()
        serializer = ProductSerializer(instance=products, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        """Create a Product View"""
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            new_product = ProductEntity(
                description=serializer.validated_data["description"],
                unit_price=serializer.validated_data["unit_price"],
                commission_percentage=serializer.validated_data["commission_percentage"]
            )
            product_service.create_product(new_product)

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductDetail(APIView):
    """Parameter dependent Views"""

    def get(self, request, pk, format=None):
        """Get a Product by pk View"""
        product = product_service.get_product_by_pk(pk)
        serializer = ProductSerializer(product)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        """Update Product data View"""
        old_product = product_service.get_product_by_pk(pk)
        serializer = ProductSerializer(
            instance=old_product, data=request.data)
        if serializer.is_valid():
            new_product = ProductEntity(
                description=serializer.validated_data["description"],
                unit_price=serializer.validated_data["unit_price"],
                commission_percentage=serializer.validated_data["commission_percentage"]
            )
            product_service.update_product(old_product, new_product)

            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        """Delete Product data View"""
        product = product_service.get_product_by_pk(pk)
        product_service.delete_product(product)

        return Response(status=status.HTTP_204_NO_CONTENT)
