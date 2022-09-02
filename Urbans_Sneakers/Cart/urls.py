from django.contrib import admin
from django.urls import path,include
from .views import add_product,clean_cart,delete_product,subtract_product,cart,add_product_cart


app_name='cart'

urlpatterns = [
    path('add_product/<int:pk>/', add_product, name='add_product'),
    path('add_product_cart/<int:pk>/', add_product_cart, name='add_product_cart'),

    path('clean_cart/', clean_cart, name='clean_cart'),

    path('delete_product/<int:pk>/', delete_product, name='delete_product'),

    path('subtract_product/<int:pk>/', subtract_product, name='subtract_product'),
    
    path('cart/', cart, name='cart'),

    
]