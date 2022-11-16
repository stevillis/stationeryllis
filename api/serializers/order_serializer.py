"""Order serializer module"""

from rest_framework import serializers

from app.models import Order


class OrderSerializer(serializers.ModelSerializer):
    """Order serializer"""

    class Meta:
        """Meta definitions"""

        model = Order
        fields = ("id", "datetime", "invoice_number", "customer", "seller")
