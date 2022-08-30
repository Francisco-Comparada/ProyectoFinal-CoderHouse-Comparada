from django.contrib import admin
from Productos.models import Category,Product,Sub_Category


@admin.register(Product)
class Product_admin(admin.ModelAdmin):
    list_display = ['category', 'model', 'price', 'coulor','description','stock','img']


@admin.register(Category)
class Category_admin(admin.ModelAdmin):
    list_display = ['category']


@admin.register(Sub_Category)
class Sub_Category_admin(admin.ModelAdmin):
    list_display = ['sub_category','img_sub_category']