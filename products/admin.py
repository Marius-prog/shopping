from django.contrib import admin
from .models import Category, Product, Seller

admin.site.register(Seller)
admin.site.register(Product)
admin.site.register(Category)