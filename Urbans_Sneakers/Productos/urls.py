from django.urls import path
from Productos.views import create_product,Shop_Category,Create_Category,List_Category

urlpatterns = [
    path('create_product/', create_product, name='create_product'),

    path('Shop_Category/<int:pk>/', Shop_Category, name='Shop'),

    path('create_Category/', Create_Category.as_view(), name='Create_article'),
    path('List_Category/', List_Category.as_view(), name='List_Category'),

   
] 