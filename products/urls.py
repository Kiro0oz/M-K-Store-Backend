from django.urls import path
# from .views import get_products, get_product
from .views import GetProductsView, RetrieveProductView, AddReviewView, ProductReviewListView

urlpatterns = [
    path('', GetProductsView.as_view(), name="get-products"),
    path('<int:id>', RetrieveProductView.as_view(), name="retrieve-product"),
    path('<int:id>/add-review/', AddReviewView.as_view(), name='add-review'),
    path('<int:id>/reviews/', ProductReviewListView.as_view(), name='product-reviews'),
]
