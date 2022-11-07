"""Product serializer module"""

from rest_framework import serializers

from app.models import Product


class ProductSerializer(serializers.ModelSerializer):
    """Product serializer"""
    class Meta:
        """Meta definitions"""
        model = Product
        fields = ("id", "description", "unit_price", "commission_percentage")
