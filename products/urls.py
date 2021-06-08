from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ProductList, CategoryViewSet

category_list = CategoryViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

category_detail = CategoryViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy',
})

router = DefaultRouter(trailing_slash=False)
router.register('categories', CategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('products/', ProductList.as_view()),
    # path('categories/', category_list, name='category-list'),
    path('categories/<int:pk>', category_detail, name='category-detail'),

]
