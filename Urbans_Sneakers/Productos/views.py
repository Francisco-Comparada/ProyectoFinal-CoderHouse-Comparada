from itertools import product
from multiprocessing import context
from pickle import NONE
from unicodedata import category
from django.shortcuts import render,redirect
from Productos.forms import Formulario_Product,Formulario_Create_Category,Formulario_Create_Sub_Category
from Productos.models import Product,Category,Sub_Category
from django.contrib.auth.decorators import login_required
import os
#------Products------------
#------superuser-------
@login_required
def create_product(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            form = Formulario_Product(request.POST, request.FILES)

            if form.is_valid():
                Product.objects.create(
                    category= form.cleaned_data['category'],
                    sub_category= form.cleaned_data['sub_category'],
                    model=form.cleaned_data['model'],
                    price=form.cleaned_data['price'],
                    coulor=form.cleaned_data['coulor'],
                    description=form.cleaned_data['description'],
                    stock = form.cleaned_data['stock'],
                    img = form.cleaned_data['img'],
                )
                
                return redirect(Shop_Category)

        elif request.method == 'GET':
            form = Formulario_Product()
            context = {'form':form}
            return render(request, 'Productos/create_product.html', context=context)
    else:
         return redirect('/')

@login_required
def delete_product(request, pk):
    if request.user.is_superuser:
        if request.method == 'GET':
            product = Product.objects.get(pk=pk)
            context = {'product':product}
            return render(request, 'Productos/delete_product.html', context=context)
        elif request.method == 'POST':
            product = Product.objects.get(pk=pk)
            product.delete()
            return redirect('/Productos/shop.html')
    else:
        return redirect('/')

@login_required
def update_product(request, pk):
    if request.user.is_superuser:
        if request.method == 'POST':
            product = Product.objects.get(id=pk)
            form = Formulario_Product(request.POST,request.FILES)
            
            if form.is_valid():
                product.category = form.cleaned_data['category']
                product.sub_category = form.cleaned_data['sub_category'],
                product.model = form.cleaned_data['model']
                product.price = form.cleaned_data['price']
                product.coulor = form.cleaned_data['coulor']
                product.description = form.cleaned_data['description']
                product.stock = form.cleaned_data['stock']
                
                if form.cleaned_data['img']:
                    product.img = form.cleaned_data ['img']


                product.save()
                return redirect('/shop')


        elif request.method == 'GET':
            product = Product.objects.get(id=pk)

            form = Formulario_Product(initial={
                                            'category':product.category,
                                            'sub_category':product.sub_category,
                                            'model':product.model, 
                                            'price':product.price,
                                            'coulor':product.coulor,
                                            'description':product.description,
                                            'stock':product.stock,
                                            'img':product.img})
        context = {'form':form}
        return render(request, 'Productos/update_product.html', context=context)
    else:
        return redirect('/')

@login_required
def create_category(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            form = Formulario_Create_Category(request.POST, request.FILES)

            if form.is_valid():
                Category.objects.create(
                    category= form.cleaned_data['category'],
                   
                )
                return redirect('/')

        elif request.method == 'GET':
            form = Formulario_Create_Category()
            context = {'form':form}
            return render(request, 'Productos/create_Category.html', context=context)
    else:
         return redirect('/')

@login_required
def create_sub_category(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            form = Formulario_Create_Sub_Category(request.POST, request.FILES)

            if form.is_valid():
                Sub_Category.objects.create(
                    category= form.cleaned_data['category'],
                    sub_category= form.cleaned_data['sub_category'],
                    img_sub_category=form.cleaned_data['img_sub_category'],
                )
                return redirect('/')

        elif request.method == 'GET':
            form = Formulario_Create_Sub_Category()
            context = {'form':form}
            return render(request, 'Productos/create_sub_category.html', context=context)
    else:
         return redirect('/')



#------superuser-------



#------user-----------

def Shop_single(request, pk):#muestra detalles de cada producto 
    if request.method == 'GET':
        product = Product.objects.get(pk=pk)
        context = {'product':product}
        return render(request, 'Productos/Shop_single.html', context=context)
        #para cuando use el boton buy o add to cart
    elif request.method == 'POST':
        product = Product.objects.get(pk=pk)
        return redirect('Productos/shop.html')

def search_products(request):#Busqueda de productos por nombe/modelo
    search = request.GET['search']
    products =Product.objects.filter(model__icontains=search)
    context = {
        'products': products
    }
    return render(request, 'Productos/search_products.html', context=context)

def Shop_Category(request, pk):#Shop vista categoria
    if request.method == 'GET':
        category_id = Category.objects.filter(pk=pk)
        products_id=Product.objects.filter(category_id=pk)
        print(len(products_id))
        context = {
            'category_id':category_id,
            'products_id':products_id
        }
        return render(request, 'Productos/Shop_Category.html', context=context)
        
def Shop_sub_Category(request, pk):#Shop vista por sub_categoria
    if request.method == 'GET':
        sub_category_id = Sub_Category.objects.filter(pk=pk)
        products_id=Product.objects.filter(sub_category_id=pk)
        print(len(products_id))
        context = {
            'sub_category_id':sub_category_id,
            'products_id':products_id
        }
        return render(request, 'Productos/Shop_sub_Category.html', context=context)


#------user-----------

