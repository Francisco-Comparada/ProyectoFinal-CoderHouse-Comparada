from django.urls import path
from Orders.views import process_order,order_list

app_name='order'

urlpatterns = [
    path('process_order/', process_order, name='process_order'),
    path('order_list/', order_list, name='order_list'),
] 