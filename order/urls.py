from django.urls import path
from .views import new_order, delete_order, process_order, get_order, get_orders

urlpatterns = [
    path('new/', new_order, name='new_order'),
    path('delete/<str:pk>/', delete_order, name='delete_order'),
    path('process/<str:pk>/', process_order, name='process_order'),
    path('get/<str:pk>/', get_order, name='get_order'),  
    path('', get_orders, name='get_orders'), 
]
