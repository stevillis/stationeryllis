"""Seller serializer module"""

from rest_framework import serializers

from app.models import Seller


class SellerSerializer(serializers.ModelSerializer):
    """Seller serializer"""
    class Meta:
        """Meta definitions"""
        model = Seller
        fields = ("id", "name", "email", "phone")
