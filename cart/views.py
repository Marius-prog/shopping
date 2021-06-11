from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from cart.models import Cart
from cart.serializer import CartSerializer


class ListCart(ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class DetailCart(ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
