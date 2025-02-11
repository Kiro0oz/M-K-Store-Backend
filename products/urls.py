from django.urls import path
# from .views import get_products, get_product
from .views import GetProductsView, RetrieveProductView

urlpatterns = [
    path('', GetProductsView.as_view(), name="get-products"),
    path('/<int:id>', RetrieveProductView.as_view(), name="retrieve-product"),
]
