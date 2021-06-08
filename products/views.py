from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .serializers import ProductAllInfoSerializer, ProductSerializer, CategorySerializer

from .models import Product, Category


class ProductList(APIView):
    """

    """

    def get(self, request):
        products = Product.objects.all()
        serializer = ProductAllInfoSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.data, status=HTTP_400_BAD_REQUEST)


class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer()
    queryset = Category.objects.all()
