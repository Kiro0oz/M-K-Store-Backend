from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .models import Cart, CartItem
from products.models import Product
from django.contrib.auth.models import User
from .serializers import CartSerializer

# Get or create a cart for the user
def get_or_create_cart(user):
    cart, created = Cart.objects.get_or_create(user=user)
    return cart

# Add products to cart
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_to_cart(request):
    data = request.data
    user_id = data.get('userId')
    products = data.get('products', [])

    if not user_id or not products:
        return Response({'error': 'User ID and products list are required'}, status=400)

    user = get_object_or_404(User, id=user_id)
    cart = get_or_create_cart(user)

    for product_data in products:
        product_id = product_data.get('productId')
        quantity = product_data.get('quantity', 1)

        if not product_id:
            continue  # Skip invalid product entries

        product = get_object_or_404(Product, id=product_id)

        # Check if item exists in cart
        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
        if not created:
            cart_item.quantity += int(quantity)
        else:
            cart_item.quantity = int(quantity)
        cart_item.save()

    return Response({'message': 'Products added to cart successfully'})

# ✅ View Cart Items
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def view_cart(request):
    cart = get_or_create_cart(request.user)
    serializer = CartSerializer(cart)
    return Response(serializer.data)

# ✅ Remove Product from Cart@api_view(['DELETE'])
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def remove_from_cart(request, cart_item_id):
    """
    Remove a specific cart item from the user's cart using cartItem ID.
    """
    cart = get_or_create_cart(request.user)
    cart_item = get_object_or_404(CartItem, cart=cart, id=cart_item_id)  # Use cartItem ID instead of product_id
    cart_item.delete()
    
    return Response({'message': 'Cart item removed successfully'})


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def clear_cart(request):
    """
    Clear all items from the user's cart.
    """
    cart = get_or_create_cart(request.user)
    cart.items.all().delete()  # Remove all cart items
    
    return Response({'message': 'Cart cleared successfully'}, status=200)