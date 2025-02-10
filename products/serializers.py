from rest_framework.serializers import ModelSerializer
from .models import Product

class ReadProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'