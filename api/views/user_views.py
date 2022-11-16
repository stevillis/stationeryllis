"""Customer views module"""

from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from api.serializers.user_serializer import UserSerializer


class UserList(GenericAPIView):
    """Non parameter dependent Views"""

    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def post(self, request, format=None):
        """Create a User View"""
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
