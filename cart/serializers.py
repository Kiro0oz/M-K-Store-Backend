from rest_framework import serializers
from .models import Cart, CartItem
from django.conf import settings 
from products.models import Product

class ProductSerializer(serializers.ModelSerializer):
    """Serializer for product details inside the cart"""
    from django.conf import settings
    class Meta:
        model = Product
        fields = ['id', 'title', 'price' , 'image']  

    def get_image(self, obj):
        """Return full image URL"""
        if obj.image:
            request = self.context.get('request')  # Get request context
            return request.build_absolute_uri(obj.image.url) if request else obj.image.url
        return None  # If no image exists

class CartItemSerializer(serializers.ModelSerializer):
    """Serializer for cart items"""
    
    product = ProductSerializer(read_only=True)  # Nested product details
    subtotal = serializers.SerializerMethodField()

    class Meta:
        model = CartItem
        fields = ['id', 'product', 'quantity', 'subtotal']

    def get_subtotal(self, obj):
        return obj.product.price * obj.quantity  # Subtotal per product

class CartSerializer(serializers.ModelSerializer):
    """Serializer for the entire cart"""
    
    items = CartItemSerializer(many=True, read_only=True)  # Include all cart items
    total_price = serializers.SerializerMethodField()  
    class Meta:
        model = Cart
        fields = ['id', 'user', 'items','total_price' , 'created_at']

    def get_total_price(self, obj):
        return sum(item.product.price * item.quantity for item in obj.items.all())
