"""Order serializer module"""

from rest_framework import serializers
from rest_framework.reverse import reverse

from app.models import Order


class OrderSerializer(serializers.ModelSerializer):
    """Order serializer"""

    endpoints = serializers.SerializerMethodField()

    class Meta:
        """Meta definitions"""

        model = Order
        fields = ("id", "datetime", "invoice_number", "customer", "seller", "endpoints")

    def get_endpoints(self, obj):
        """Get Order available endpoints"""
        request = self.context.get("request")

        return {
            "GET": reverse("orders-detail", kwargs={"pk": obj.pk}, request=request),
            "PUT": reverse("orders-detail", kwargs={"pk": obj.pk}, request=request),
            "DELETE": reverse("orders-detail", kwargs={"pk": obj.pk}, request=request),
        }
