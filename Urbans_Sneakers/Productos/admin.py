from django.contrib import admin
from Productos.models import Category,Product

# Register your models here.
@admin.register(Product)
class Product_admin(admin.ModelAdmin):
    list_display = ['category', 'model', 'price', 'coulor','description','stock','img']
@admin.register(Category)
class Category_admin(admin.ModelAdmin):
    list_display = ['category', 'img_category']