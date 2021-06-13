from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer

from cart.models import Cart
from products.serializers import ProductSerializer


class CartSerializer(ModelSerializer):
    products = ProductSerializer(read_only=True, many=True)

    class Meta:
        model = Cart
        fields = ('cart_id', 'created_at', 'products')


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'id')
