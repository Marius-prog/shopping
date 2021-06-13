from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Category, Product


class CategorySerializer(ModelSerializer):
    random_photo = SerializerMethodField()

    def get_random_photo(self, obj):
        try:
            return obj.products.first().photo
        except:
            return ""

    class Meta:
        model = Category
        fields = (
            'id',
            'name',
            'random_photo'
        )


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'id',
            'photo',
            'price',
            'title',
            'category',

        )


class ProductsAllInfoSerializer(ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Product
        fields = (
            'id',
            'photo',
            'price',
            'title',
            'category',

        )


class ProductListViewSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'id',
            'photo',
            'price',
            'title',

        ]
