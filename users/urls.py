from django.urls import path, include
from .views import register, current_user, forgetPassword, reset_password
from rest_framework_simplejwt.views import TokenObtainPairView


urlpatterns = [
    path('register/', register, name="register"),
    path('userinfo/', current_user, name="user_info"),
    path('login/', TokenObtainPairView.as_view()),
    path('password/reset/',forgetPassword, name='forget_password'), 
    path('password/reset/confirm/<str:token>',reset_password, name='reset_password'), 


]
