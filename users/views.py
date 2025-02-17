from datetime import datetime, timedelta
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework import status
from .serializers import SignUpSerializer , UserSerializer
from rest_framework.permissions import IsAuthenticated
from django.utils.crypto import get_random_string
from django.core.mail import send_mail

@api_view(['POST'])
def register(request):
    data = request.data
    user = SignUpSerializer(data = data)

    if user.is_valid():
        if not User.objects.filter(username=data['email']).exists():  
            user = User.objects.create(
                username = data['username'],
                first_name = data['first_name'], 
                last_name = data['last_name'],
                email = data['email'], 
                password = make_password(data['password'])
            )
            return Response({'details': 'Your account created successfully'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'error': 'This email already exists'}, status=status.HTTP_400_BAD_REQUEST)

    else:
        return Response(user.errors, status=status.HTTP_400_BAD_REQUEST)
    
    

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def current_user(request):
    user = UserSerializer(request.user)
    return Response(user.data)


def get_current_host(request):
    protocol = "https" if request.is_secure() else "http"
    host = request.get_host()
    return f'{protocol}://{host}/'.format(protocol=protocol, host=host)

@api_view(['POST'])
def forgetPassword(request):
    data = request.data
    user = get_object_or_404(User,email=data['email'])
    token = get_random_string(40)
    expire_data = datetime.now()+timedelta(minutes=30)
    user.profile.reset_password_token = token
    user.profile.rest_password_token_expiry = expire_data
    user.profile.save()
    host = get_current_host(request)
    link = f"{host}api/auth/password/reset/confirm/{token}".format(token=token)
    body = "Your password reset link is : {link}".format(link=link)
    send_mail(
        "Password reset from eMarket",
        body,
        "eMarket@gmail.com",
        [data['email']]
    )
    return Response({'details': 'Password reset sent to {email}'.format(email=data['email'])})


@api_view(['POST'])
def reset_password(request, token):
    data = request.data

    user = get_object_or_404(User, profile__rest_password_token=token)

    # Ensure profile exists
    if not hasattr(user, 'profile'):
        return Response({'error': 'User profile not found'}, status=status.HTTP_404_NOT_FOUND)

    if user.profile.rest_password_token_expiry.replace(tzinfo=None) < datetime.now():
        return Response({'error': 'Token has expired'}, status=status.HTTP_400_BAD_REQUEST)

    if data.get('password') != data.get('confirmPassword'):
        return Response({'error': 'Passwords do not match'}, status=status.HTTP_400_BAD_REQUEST)

    user.password = make_password(data['password'])
    user.profile.rest_password_token = ""
    user.profile.rest_password_token_expiry = None
    user.profile.save()
    user.save()

    return Response({'details': 'Password reset successful'})