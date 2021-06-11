from django.db import models

from products.models import Product, Seller


class Cart(models.Model):
    cart_id = models.OneToOneField(Seller, on_delete=models.CASCADE, primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    products = models.ManyToManyField(Product)

    class Meta:
        ordering = ['cart_id', '-created_at']

    def __str__(self):
        return f'{self.cart_id}, cart'
