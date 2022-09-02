
from django.shortcuts import render,redirect
from .models import Start_Banner,Featured_Products
from .forms import Form_start_Banner,Form_Featured_Products
from django.contrib.auth.decorators import login_required




@login_required(login_url='/users/login')
def create_banner(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            form = Form_start_Banner(request.POST,request.FILES)
            if form.is_valid():
                    Start_Banner.objects.create(
                        banner=form.cleaned_data['banner'],
                        title_banner=form.cleaned_data['title_banner'],
                        sub_tittle_banner = form.cleaned_data['sub_tittle_banner'],
                        text_banner = form.cleaned_data['text_banner'],
                        img_banner = form.cleaned_data['img_banner'],
                    )
                    return redirect('/customize_page/')
        elif request.method == 'GET':
            form = Form_start_Banner()
            context = {'form':form}
        return render(request, 'customize_page/create_banner.html', context=context)
    else:
        return redirect('/users/login/')




@login_required(login_url='/users/login')
def delete_banner(request, pk):
    if request.user.is_superuser:
        if request.method == 'GET':
            banner = Start_Banner.objects.get(pk=pk)
            context = {'banner':banner}
            return render(request, 'customize_page/delete_banner.html', context=context)

        elif request.method == 'POST':
            banner = Start_Banner.objects.get(pk=pk)
            banner.delete()
            return redirect('/customize_page/')
    else:
        return redirect('/users/login/')




@login_required(login_url='/users/login')
def select_banner(request):
    if request.user.is_superuser:
            banners = Start_Banner.objects.all() #Trae todos
            context = {
                'banners':banners
            }
            return render(request, 'customize_page/select_banner.html', context=context)
    else:
        return redirect('/users/login/')




@login_required(login_url='/users/login')
def create_Featured_Products(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            form = Form_Featured_Products(request.POST,request.FILES)
            if form.is_valid():
                    Featured_Products.objects.create(
                        product=form.cleaned_data['product'],
                    )
                    return redirect('/customize_page/')
        elif request.method == 'GET':
            form = Form_Featured_Products()
            context = {'form':form}
        return render(request, 'customize_page/create_Featured_Products.html', context=context)
    else:
        return redirect('/users/login/')




@login_required(login_url='/users/login')
def delete_Featured_Products(request, pk):
    if request.user.is_superuser:
        if request.method == 'GET':
            product = Featured_Products.objects.get(pk=pk)
            context = {'product':product}
            return render(request, 'customize_page/delete_Featured_Products.html', context=context)

        elif request.method == 'POST':
            product = Featured_Products.objects.get(pk=pk)
            product.delete()
            return redirect('/customize_page/')
    else:
        return redirect('/users/login/')




@login_required(login_url='/users/login')
def select_Featured_Products(request):
    if request.user.is_superuser:
            products = Featured_Products.objects.all() #Trae todos
            context = {
                'products':products
            }
            return render(request, 'customize_page/select_Featured_Products.html', context=context)
    else:
        return redirect('/users/login/')