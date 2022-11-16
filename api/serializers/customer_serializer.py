"""Customer serializer module"""
from rest_framework import serializers
from rest_framework.reverse import reverse

from app.models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    """Customer serializer"""

    endpoints = serializers.SerializerMethodField()

    class Meta:
        """Meta definitions"""

        model = Customer
        fields = ("id", "name", "email", "phone", "endpoints")

    def get_endpoints(self, obj):
        """Get Customer available endpoints"""
        request = self.context.get("request")

        return {
            "GET": reverse("customers-detail", kwargs={"pk": obj.pk}, request=request),
            "PUT": reverse("customers-detail", kwargs={"pk": obj.pk}, request=request),
            "DELETE": reverse(
                "customers-detail", kwargs={"pk": obj.pk}, request=request
            ),
        }
