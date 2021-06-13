from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Category(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Product(models.Model):
    photo = models.URLField(max_length=500)
    price = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    title = models.CharField(max_length=250)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
