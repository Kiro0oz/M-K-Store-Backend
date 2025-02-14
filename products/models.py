from django.db import models
from category.models import Category
from django.contrib.auth.models import User

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
    



class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    rating = models.IntegerField(default=0)
    comment = models.TextField(max_length=1000, default="" , blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.user.username} - {self.product.title}"
        