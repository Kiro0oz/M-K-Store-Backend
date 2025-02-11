from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Product

class ReadProductSerializer(ModelSerializer):
    category_name = SerializerMethodField()
    class Meta:
        model = Product
        fields = [
            "id", "title", "description", "created_at", "updated_at",
            "quantity", "discount", "price", "image", "category_name"
        ]

    def get_category_name(self, obj):
        return obj.category.name if obj.category else None