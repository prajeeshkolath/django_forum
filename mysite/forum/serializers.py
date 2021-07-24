from rest_framework import serializers

from forum.models import Category

class CategorySerializer(serializers.ModelSerializer):
    """Serializer for Category model"""

    class Meta:
        model = Category
        exclude = []
