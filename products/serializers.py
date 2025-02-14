from rest_framework.serializers import ModelSerializer, SerializerMethodField
from rest_framework import serializers
from .models import Product, Review

class ReadProductSerializer(ModelSerializer):
    category_name = SerializerMethodField()
    class Meta:
        model = Product
        fields = [
            "id", "title", "description", "created_at", "updated_at",
            "quantity", "discount", "price", "image", "category_name"
        ]

    def get_category_name(self, obj):
        return obj.category.name if obj.category else None
    

class ReviewSerializer(ModelSerializer):
    """
     Serializer for Review model. 
    """
    username = serializers.CharField(source='user.username', read_only=True)
    product = serializers.CharField(source='product.title',read_only=True)
    class Meta:
        model = Review
        fields = ['id', 'rating', 'comment', 'created_at', 'product', 'username']