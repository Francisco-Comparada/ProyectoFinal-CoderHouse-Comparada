from django.urls import path
from .views import create_banner,create_Featured_Products,delete_banner,select_banner,select_Featured_Products,delete_Featured_Products


urlpatterns = [
    path('create_banner/', create_banner, name='create_banner'),
    path('select_banner/', select_banner, name='select_banner'),
    path('delete_banner/<int:pk>/', delete_banner, name='delete_banner'),

    
    path('create_Featured_Products/', create_Featured_Products, name='create_Featured_Products'),
    path('select_Featured_Products/', select_Featured_Products, name='select_Featured_Products'),
    path('delete_Featured_Products/<int:pk>/', delete_Featured_Products, name='delete_Featured_Products'),
 
]