from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from .models import Product, Review
from .serializers import ReadProductSerializer, ReviewSerializer
from django.core.cache import cache
from datetime import timedelta
from rest_framework.filters import SearchFilter
from rest_framework import status
from rest_framework.exceptions import APIException
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

# Define a custom pagination class 
class CustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class CustomNotFound(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = "No products found."
    default_code = "not_found"

    def __init__(self, detail=None):
        if detail is None:
            detail = self.default_detail
        self.detail = {"error": detail}

class GetProductsView(ListAPIView):
    """
    API endpoint to get all products (with caching, search, and pagination).
    Only products with quantity > 0 are returned.
    """
    serializer_class = ReadProductSerializer
    filter_backends = (SearchFilter, DjangoFilterBackend)
    search_fields = ['title', 'description']
    pagination_class = CustomPagination

    def get_queryset(self):
        limit = self.request.query_params.get("limit", None)

        # Try to get the cached products
        products = cache.get('products')

        if not products:
            queryset = Product.objects.filter(quantity__gt=0).order_by('-created_at')

            if not queryset.exists():
                raise CustomNotFound('No products found.')

            # Serialize and cache the data
            products = list(queryset.values())  
            cache.set('products', products, timeout=timedelta(hours=2).total_seconds())

        # Apply limit if provided in query params
        if limit and limit.isdigit():
            return Product.objects.filter(id__in=[p["id"] for p in products[:int(limit)]]) 

        return Product.objects.filter(id__in=[p["id"] for p in products])  

class RetrieveProductView(RetrieveAPIView):
    """
    API endpoint to retrieve a single product by its id.
    Only products with quantity > 0 are returned.
    """
    serializer_class = ReadProductSerializer
    lookup_field = 'id'
    queryset = Product.objects.filter(quantity__gt=0)

# Add Review Class


class AddReviewView(CreateAPIView):
    """
    API endpoint to add a new review for a product In Authenticated Users.
    """
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        product_id = self.kwargs.get('id')  # Get product ID from URL

        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(product=product, user=request.user)

        return Response(
            {"message": "Comment Added Successfully"},
            status=status.HTTP_201_CREATED
        )


class ProductReviewListView(ListAPIView):
    """
    API endpoint to list all reviews for a product.
    """
    serializer_class = ReviewSerializer

    def get_queryset(self):
        product_id = self.kwargs.get('id')
        return Review.objects.filter(product_id=product_id)

