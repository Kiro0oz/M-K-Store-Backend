from django.urls import path, include
from .views import register, current_user
from rest_framework_simplejwt.views import TokenObtainPairView
from dj_rest_auth.views import PasswordResetView, PasswordResetConfirmView

urlpatterns = [
    path('register/', register, name="register"),
    path('userinfo/', current_user, name="user_info"),
    path('login/', TokenObtainPairView.as_view()),
    path('password/reset/', PasswordResetView.as_view(), name='password_reset'),
    path('password/reset/confirm/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),


]
