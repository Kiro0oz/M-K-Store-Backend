from django.urls import path
# from .views import get_products, get_product
from .views import GetProductsView, RetrieveProductView

urlpatterns = [
    path('api/products/', GetProductsView.as_view(), name="get-products"),
    path('api/products/<int:id>/', RetrieveProductView.as_view(), name="retrieve-product"),
]
