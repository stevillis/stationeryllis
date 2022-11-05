"""Customer serializer module"""

from rest_framework import serializers

from app.models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    """Customer serializer"""
    class Meta:
        """Meta definitions"""
        model = Customer
        fields = ('name', 'email', 'phone')
