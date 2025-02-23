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

    rating = serializers.IntegerField(required=True) 
    comment = serializers.CharField(required=True) 
    class Meta:
        model = Review
        fields = ['id', 'rating', 'comment', 'created_at', 'product', 'username']

    def validate_comment(self, value):
        """
        Ensure that the comment is not empty or just whitespace.
        """
        if not value.strip():  # Prevent empty or whitespace-only comments
            raise serializers.ValidationError("Comment is required.")
        return value
    
    def validate_rating(self, value):
        """Ensure that the rating is within the valid range (1-5)."""
        if value not in [1, 2, 3, 4, 5]:  # Only accept ratings between 1 and 5
            raise serializers.ValidationError("Rating must be between 1 and 5.")
        return value