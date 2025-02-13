from django.contrib import admin
from django.urls import path, include
# from rest_framework_simplejwt.views import TokenObtainPairView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/products', include('products.urls')),
    path('api/category', include('category.urls')),
    path('api/auth/', include('account.urls')),
    # path('api/token/', TokenObtainPairView.as_view()),
    

]
