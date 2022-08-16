from django.urls import path
from Productos.views import create_product,Shop_Category,Create_Category,Shop_single,search_products

urlpatterns = [
    path('create_product/', create_product, name='create_product'),

    path('Shop_Category/<int:pk>/', Shop_Category, name='Shop'),
    path('Shop_single/<int:pk>/', Shop_single, name='Shop_single'),
    path('create_Category/', Create_Category.as_view(), name='Create_article'),
    path('search_products/', search_products, name='search_products'),

   
] 