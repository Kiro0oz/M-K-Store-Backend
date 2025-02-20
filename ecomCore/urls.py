from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenObtainPairView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/products/', include('products.urls')),
    path('api/order/', include('order.urls')),
    path('api/category/', include('category.urls')),
    path('api/cart/', include('cart.urls')),
    path('api/auth/', include('users.urls')),
    path('accounts/', include('allauth.urls')),
    path('api/token/', TokenObtainPairView.as_view()),
    # path('auth/', include('dj_rest_auth.urls')),  # Include authentication endpoints
    # path('auth/registration/', include('dj_rest_auth.registration.urls')),  # Registration
    # path('auth/social/', include('allauth.urls')),  # Social authentication
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
