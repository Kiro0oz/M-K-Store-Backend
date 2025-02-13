from django.urls import path
from .views import register, current_user
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('register/', register, name="register"),
    path('userinfo/', current_user, name="user_info"),
    path('login/', TokenObtainPairView.as_view()),

]
