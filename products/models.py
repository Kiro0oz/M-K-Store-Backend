from django.db import models
from category.models import Category

class Product(models.Model):
    title = models.CharField(max_length=225)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    quantity = models.IntegerField(default=0)
    discount = models.DecimalField(max_digits=100, decimal_places=0)
    price = models.FloatField(default=0)
    image = models.ImageField(upload_to='media/product_images')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    def __str__(self):
        return self.title