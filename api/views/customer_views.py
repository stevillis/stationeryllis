"""Customer views module"""

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers.customer_serializer import CustomerSerializer
from api.services.customer_service import get_all_customers


class CustomerList(APIView):
    """Non parameter dependent views"""

    def get(self, request, format=None):
        """GET view"""
        customers = get_all_customers()
        serializer = CustomerSerializer(instance=customers, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
