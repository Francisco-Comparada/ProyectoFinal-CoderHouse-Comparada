from django.shortcuts import render,redirect
from Productos.forms import Formulario_Product
from Productos.models import Product

def create_product(request):
    
    if request.method == 'POST':
        form = Formulario_Product(request.POST, request.FILES)

        if form.is_valid():
            Product.objects.create(
                category= form.cleaned_data['category'],
                model=form.cleaned_data['model'],
                price=form.cleaned_data['price'],
                coulor=form.cleaned_data['coulor'],
                description=form.cleaned_data['description'],
                stock = form.cleaned_data['stock'],
                img = form.cleaned_data['img'],
            )
            
            return redirect(list_products)

    elif request.method == 'GET':
        form = Formulario_Product()
        context = {'form':form}
        return render(request, 'Productos/create_product.html', context=context)


def list_products(request):
    products = Product.objects.all() #Trae todos
    context = {
        'products':products
    }
    return render(request, 'Productos/list_products.html', context=context)
