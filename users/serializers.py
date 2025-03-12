from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the User model.
    Handles conversion between User instances and JSON data.
    Validates that name, email, and age are provided and that email is unique.
    """
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'age']