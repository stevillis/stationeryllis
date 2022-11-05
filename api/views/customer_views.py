"""Customer views module"""

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.entities.customer_entity import CustomerEntity
from api.serializers.customer_serializer import CustomerSerializer
from api.services import customer_service


class CustomerList(APIView):
    """Non parameter dependent Views"""

    def get(self, request, format=None):
        """Get all Customers View"""
        customers = customer_service.get_all_customers()
        serializer = CustomerSerializer(instance=customers, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        """Create a Customer View"""
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            new_customer = CustomerEntity(
                name=serializer.validated_data["name"],
                email=serializer.validated_data["email"],
                phone=serializer.validated_data["phone"]
            )
            customer_service.create_customer(new_customer)

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomerDetail(APIView):
    """Parameter dependent Views"""

    def get(self, request, pk, format=None):
        """Get a Customer by pk View"""
        customer = customer_service.get_customer_by_pk(pk)
        serializer = CustomerSerializer(customer)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        """Update Customer data View"""
        old_customer = customer_service.get_customer_by_pk(pk)
        serializer = CustomerSerializer(
            instance=old_customer, data=request.data)
        if serializer.is_valid():
            new_customer = CustomerEntity(
                name=serializer.validated_data["name"],
                email=serializer.validated_data["email"],
                phone=serializer.validated_data["phone"]
            )
            customer_service.update_customer(old_customer, new_customer)

            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        """Delete Customer data View"""
        customer = customer_service.get_customer_by_pk(pk)
        customer_service.delete_customer(customer)
        return Response(status=status.HTTP_204_NO_CONTENT)
