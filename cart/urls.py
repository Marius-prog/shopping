from django.urls import path, include

from cart.views import ListCart, DetailCart

cart_list = ListCart.as_view({
    'get': 'list',
    'post': 'create',
})

cart_detail = DetailCart.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'
})

urlpatterns = [

    path('carts/', cart_list, name='cart-list'),
    path('carts/<int:pk>/', cart_detail, name='cart-detail'),

]
