from itertools import product
from django.shortcuts import render,redirect
from .cart import Cart
from Productos.models import Product
from django.contrib.auth.decorators import login_required

@login_required
def cart(request):
    return render (request,'Cart/cart.html')

@login_required
def add_product(request,pk):
    if request.user.is_authenticated:
        cart=Cart(request)
        product=Product.objects.get(id=pk)
        cart.add(product=product)
        return redirect ('/Cart/cart')
    else:
        return redirect ('/users/login')
        
@login_required
def delete_product(request,pk):
    cart=Cart(request)
    product=Product.objects.get(id=pk)
    cart.delete(product=product)
    return redirect ('/Cart/cart')

@login_required
def subtract_product(request,pk):
    cart=Cart(request)
    product=Product.objects.get(id=pk)
    cart.subtract(product=product)
    return redirect ('/Cart/cart')

@login_required   
def clean_cart(request):
    cart=Cart(request)
    cart.clean_cart()
    return redirect ('/Cart/cart')
