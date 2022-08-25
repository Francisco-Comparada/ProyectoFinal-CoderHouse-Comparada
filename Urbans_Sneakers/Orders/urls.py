from django.urls import path
from Orders.views import process_order

app_name='order'
urlpatterns = [
    path('process_order/', process_order, name='process_order'),
] 