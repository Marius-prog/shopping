from django.contrib.auth.models import User
from rest_framework.viewsets import ModelViewSet

from cart.models import Cart
from cart.serializer import CartSerializer, UserSerializer


class ListCart(ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class DetailCart(ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
