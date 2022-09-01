from django.contrib import admin
from .models import Order,Order_line

@admin.register(Order)
class Order_admin(admin.ModelAdmin):
    list_display = ['user', 'created_id',]
    
@admin.register(Order_line)
class Order_line_admin(admin.ModelAdmin):
    list_display = ['user', 'product_id', 'order_id', 'cant', 'created_id']