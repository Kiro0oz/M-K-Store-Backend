# products/views.py
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Product
from .serializers import ReadProductSerializer
from django.core.cache import cache
from datetime import timedelta
from rest_framework.filters import SearchFilter
from rest_framework import status
from rest_framework.exceptions import APIException
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination

# Define a custom pagination class (optional—you can adjust page size as needed)
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
    # You can add valid filterset fields if your model had them; for now, we’ll omit it.
    pagination_class = CustomPagination

    def get_queryset(self):
        limit = self.request.query_params.get("limit", None)
        # Try to get the cached queryset
        products = cache.get('products')
        if not products:
            products = Product.objects.filter(quantity__gt=0).order_by('-created_at')

            if not products.exists():
                raise CustomNotFound('No products found.')
            # Cache the queryset for 2 hours (you can adjust the timeout as needed)
            cache.set('products', products, timeout=timedelta(hours=2).total_seconds())

        if limit and limit.isdigit():  # 🔹 Apply limit if provided in query params
            return products[:int(limit)]

        return products

class RetrieveProductView(RetrieveAPIView):
    """
    API endpoint to retrieve a single product by its id.
    Only products with quantity > 0 are returned.
    """
    serializer_class = ReadProductSerializer
    lookup_field = 'id'
    queryset = Product.objects.filter(quantity__gt=0)
