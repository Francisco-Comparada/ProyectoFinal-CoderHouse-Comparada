from django.urls import path
from Productos.views import create_product,Shop_Category,create_category,Shop_single,search_products,delete_product,update_product,create_sub_category,Shop_sub_Category,filter_products,filter_Category,filter_sub_Category,descripcion_product,filter_search_products,filter_list_products
urlpatterns = [
    
    path('create_product/', create_product, name='create_product'),
    path('create_Category/', create_category, name='create_category'),
    path('create_sub_category/', create_sub_category, name='create_sub_category'),
    path('update_product/<int:pk>/', update_product, name='update_product'),
    path('delete_product/<int:pk>/', delete_product, name='delete_product'),
    path('descripcion_product/<int:pk>/', descripcion_product, name='descripcion_product'),
    path('filter_search_products/', filter_search_products, name='filter_search_products'),
    path('filter_list_products/', filter_list_products, name='filter_list_products'),

    path('Shop_Category/<int:pk>/', Shop_Category, name='Shop_Category'),
    path('Shop_sub_Category/<int:pk>/', Shop_sub_Category, name='Shop_sub_Category'),
    path('Shop_single/<int:pk>/', Shop_single, name='Shop_single'),


    path('filter_products/', filter_products, name='filter_products'),
    path('filter_Category/<int:pk>/', filter_Category, name='filter_Category'),
    path('filter_sub_Category/<int:pk>/', filter_sub_Category, name='filter_sub_Category'),

    path('search_products/', search_products, name='search_products'),

    


   
] 