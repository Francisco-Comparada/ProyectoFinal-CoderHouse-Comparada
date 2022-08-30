from django.shortcuts import render

from Cart.cart import Cart

def index(request):
    cart=Cart(request)
    return render (request, 'General/index.html')
    
def shop(request):
    return render (request, 'General/shop.html')

def setting(request):
    return render (request, 'General/setting.html')

def base(request):
    return render (request, 'General/base.html')

def about(request):
    return render (request, 'General/about.html')

def customize_page(request):
    return render (request, 'General/customize_page.html')
    