from itertools import product
from django.shortcuts import render,redirect
from .cart import Cart
from Productos.models import Product

def cart(request):
    return render (request,'Cart/cart.html')

def add_product(request,pk):
    cart=Cart(request)
    product=Product.objects.get(id=pk)
    cart.add(product=product)
    return redirect ('/Cart/cart')

def delete_product(request,pk):
    cart=Cart(request)
    product=Product.objects.get(id=pk)
    cart.delete(product=product)
    return redirect ('/Cart/cart')

def subtract_product(request,pk):
    cart=Cart(request)
    product=Product.objects.get(id=pk)
    cart.subtract(product=product)
    return redirect ('/Cart/cart')

    
def clean_cart(request):
    cart=Cart(request)
    cart.clean_cart()
    return redirect ('/Cart/cart')