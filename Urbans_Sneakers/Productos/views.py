from itertools import product
from multiprocessing import context
from unicodedata import category
from django.shortcuts import render,redirect
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from Productos.forms import Formulario_Product
from Productos.models import Product,Category

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
            
            return redirect(Shop_Category)

    elif request.method == 'GET':
        form = Formulario_Product()
        context = {'form':form}
        return render(request, 'Productos/create_product.html', context=context)

#---------------------------------------------------------------------------------------

def Shop_Category(request, pk):
    if request.method == 'GET':
        category_id = Category.objects.filter(pk=pk)
        products_id=Product.objects.filter(category_id=pk)
        print(len(products_id))
        context = {
            'category_id':category_id,
            'products_id':products_id
        }
        return render(request, 'Productos/Shop_Category.html', context=context)

class Create_Category(CreateView):
    model = Category
    template_name = 'Productos/create_Category.html'
    fields = '__all__'
    success_url = '/Productos/create_product/'

class List_Category(ListView):
    model = Category
    template_name = 'Productos/List_Category.html'
