"""Product serializer module"""

from rest_framework import serializers
from rest_framework.reverse import reverse

from app.models import Product


class ProductSerializer(serializers.ModelSerializer):
    """Product serializer"""

    endpoints = serializers.SerializerMethodField()

    class Meta:
        """Meta definitions"""

        model = Product
        fields = (
            "id",
            "description",
            "unit_price",
            "commission_percentage",
            "endpoints",
        )

    def get_endpoints(self, obj):
        """Get Product available endpoints"""
        # Avoid AttributeError when self.context is a set instance
        request = None
        if isinstance(self.context, dict):
            request = self.context.get("request")

        return {
            "GET": reverse("products-detail", kwargs={"pk": obj.pk}, request=request),
            "PUT": reverse("products-detail", kwargs={"pk": obj.pk}, request=request),
            "DELETE": reverse(
                "products-detail", kwargs={"pk": obj.pk}, request=request
            ),
        }
