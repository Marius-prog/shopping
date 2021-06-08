from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Category, Product


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id',
            'name',
            'slug',
        )


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'category',
            'name',
            'slug',
            'image',
            'description',
            'price',
            'available',
            'created',
            'updated',
        )


class ProductAllInfoSerializer(ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Product
        fields = (
            'category',
            'name',
            'slug',
            'image',
            'description',
            'price',
            'available',
            'created',
            'updated',
        )
