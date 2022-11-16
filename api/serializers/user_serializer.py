"""User serializer module"""

from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """User serializer"""

    class Meta:
        """Meta definitions"""

        model = User
        fields = ("username", "password")

    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data["password"])
        user.save()

        return user
