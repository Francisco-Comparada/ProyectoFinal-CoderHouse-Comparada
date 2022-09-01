from django.shortcuts import render,redirect
from .cart import Cart
from Productos.models import Product
from django.contrib.auth.decorators import login_required




@login_required(login_url='/users/login')
def cart(request):
    return render (request,'Cart/cart.html')




@login_required(login_url='/users/login')
def add_product(request,pk):
    cart=Cart(request)
    product=Product.objects.get(id=pk)
    cart.add(product=product)
    return redirect ('/Productos/Shop_single/%d/?valido'%pk)




@login_required(login_url='/users/login')
def delete_product(request,pk):
    cart=Cart(request)
    product=Product.objects.get(id=pk)
    cart.delete(product=product)
    return redirect ('/Cart/cart')




@login_required(login_url='/users/login')
def subtract_product(request,pk):
    cart=Cart(request)
    product=Product.objects.get(id=pk)
    cart.subtract(product=product)
    return redirect ('/Cart/cart')




@login_required(login_url='/users/login')  
def clean_cart(request):
    cart=Cart(request)
    cart.clean_cart()
    return redirect ('/Cart/cart')
