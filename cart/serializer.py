from rest_framework.serializers import ModelSerializer

from cart.models import Cart
from products.serializers import SellerSerializer, ProductSerializer


class CartSerializer(ModelSerializer):
    cart_id = SellerSerializer(read_only=True, many=False)
    products = ProductSerializer(read_only=True, many=True)

    class Meta:
        model = Cart
        fields = ('cart_id', 'created_at', 'products')
