from django.urls import path
from Productos.views import create_product,Shop_Category,Create_Category,Shop_single,search_products,delete_product,update_product

urlpatterns = [
    path('create_product/', create_product, name='create_product'),
    path('Shop_Category/<int:pk>/', Shop_Category, name='Shop'),
    path('delete_product/<int:pk>/', delete_product, name='delete_product'),
    path('update_product/<int:pk>/', update_product, name='update_product'),
    path('Shop_single/<int:pk>/', Shop_single, name='Shop_single'),
    path('create_Category/', Create_Category.as_view(), name='Create_article'),
    path('search_products/', search_products, name='search_products'),

   
] 