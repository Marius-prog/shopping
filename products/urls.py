from django.urls import path, include
from .views import ProductList, CategoryViewSet, ProductListAPIView, ProductDetail, ProductListView

# ReportView
from rest_framework.routers import DefaultRouter

category_list = CategoryViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

category_detail = CategoryViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'
})

router = DefaultRouter(trailing_slash='optional')
router.register('shop', CategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('products/', ProductList.as_view()),
    path('handle-products/<int:pk>', ProductDetail.as_view()),
    path('products-filter/', ProductListAPIView.as_view()),

    path('categories/', category_list, name='category-list'),
    path('categories/<int:pk>/', category_detail, name='category-detail'),

    path('api/', ProductListView.as_view(), name='api-detail'),

]
