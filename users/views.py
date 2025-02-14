from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework import status
from .serializers import SignUpSerializer , UserSerializer
from rest_framework.permissions import IsAuthenticated

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