from django.urls import path
from Productos.views import create_product,Shop_Category,create_category,Shop_single,search_products,delete_product,update_product,create_sub_category,Shop_sub_Category

urlpatterns = [
    path('create_product/', create_product, name='create_product'),

    path('Shop_Category/<int:pk>/', Shop_Category, name='Shop_Category'),
    path('Shop_sub_Category/<int:pk>/', Shop_sub_Category, name='Shop_sub_Category'),

    path('delete_product/<int:pk>/', delete_product, name='delete_product'),

    path('update_product/<int:pk>/', update_product, name='update_product'),

    path('Shop_single/<int:pk>/', Shop_single, name='Shop_single'),

    path('create_Category/', create_category, name='create_category'),

    path('search_products/', search_products, name='search_products'),

    path('create_sub_category/', create_sub_category, name='create_sub_category'),


   
] 