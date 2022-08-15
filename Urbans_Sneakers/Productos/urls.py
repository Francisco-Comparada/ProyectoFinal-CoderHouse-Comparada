from django.urls import path
from Productos.views import create_product, list_products

urlpatterns = [
    path('create_product/', create_product, name='create_product'),
    path('list_products/', list_products, name='list_products'),

   
] 