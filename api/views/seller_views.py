"""Seller views module"""

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers.seller_serializer import SellerSerializer
from api.services import seller_service


class SellerList(APIView):
    """Non parameter dependent Views"""

    def get(self, request, format=None):
        """Get all Sellers View"""
        sellers = seller_service.get_all_sellers()
        serializer = SellerSerializer(instance=sellers, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        """Create a Seller View"""
        serializer = SellerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SellerDetail(APIView):
    """Parameter dependent Views"""

    def get(self, request, pk, format=None):
        """Get a Seller by pk View"""
        seller = seller_service.get_seller_by_pk(pk)
        serializer = SellerSerializer(seller)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        """Update Seller data View"""
        old_seller = seller_service.get_seller_by_pk(pk)
        serializer = SellerSerializer(
            instance=old_seller,
            data=request.data
        )
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        """Delete Seller data View"""
        seller = seller_service.get_seller_by_pk(pk)
        seller_service.delete_seller(seller)

        return Response(status=status.HTTP_204_NO_CONTENT)
