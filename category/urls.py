from django.urls import path
from .views import GetAllCategories,RetrieveCategory


urlpatterns = [
    path('', GetAllCategories.as_view(), name='get_all_categories'),
    path('<int:id>', RetrieveCategory.as_view(), name='get_category_by_id'),
    
]