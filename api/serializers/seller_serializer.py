"""Seller serializer module"""

from rest_framework import serializers
from rest_framework.reverse import reverse

from app.models import Seller


class SellerSerializer(serializers.ModelSerializer):
    """Seller serializer"""

    endpoints = serializers.SerializerMethodField()

    class Meta:
        """Meta definitions"""

        model = Seller
        fields = ("id", "name", "email", "phone", "endpoints")

    def get_endpoints(self, obj):
        """Get Seller available endpoints"""
        request = self.context.get("request")

        return {
            "GET": reverse("sellers-detail", kwargs={"pk": obj.pk}, request=request),
            "PUT": reverse("sellers-detail", kwargs={"pk": obj.pk}, request=request),
            "DELETE": reverse("sellers-detail", kwargs={"pk": obj.pk}, request=request),
        }
