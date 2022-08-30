
from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from users.forms import User_registration_form,User_edit_form
from users.models import User_profile
from django.contrib.auth.models import User



def login_request(request):#inicio de sesion
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                context = {'message':f'Bienvenido {username}!! :D'}
                return render(request, 'General/index.html', context = context)

        form = AuthenticationForm()
        return render(request, 'users/login.html', {'error': 'Formulário inválido', 'form': form})

    elif request.method == 'GET':
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})


def register(request):#registro 
    if request.method == 'POST':
        form = User_registration_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            context = {'errors':form.errors}
            form = User_registration_form()
            context['form'] = form
            return render(request, 'users/register.html', context)

    elif request.method == 'GET':
        form = User_registration_form()
        return render(request, 'users/register.html', {'form': form})


def create_profile(request):#crea el perfil por primera vez
    if request.method == 'POST':
        form = User_edit_form(request.POST,request.FILES)
        user_=User.objects.get(username=request.user)
        if form.is_valid():
                User_profile.objects.create(
                    user=user_,
                    first_name=form.cleaned_data['first_name'],
                    last_name=form.cleaned_data['last_name'],
                    phone=form.cleaned_data['phone'],
                    address = form.cleaned_data['address'],
                    image = form.cleaned_data['image'],
                )
                return redirect('/')
    elif request.method == 'GET':
        form = User_edit_form(initial={
                                    'user':request.user.username,                                                               
        })
        context = {'form':form}
    return render(request, 'users/create_profile.html', context=context)


def edit_profile(request):#edita el perfil
    if request.method == 'POST':
        form = User_edit_form(request.POST,request.FILES)
        user_=User.objects.get(username=request.user)
        edituser=User_profile.objects.get(user=user_)
        if form.is_valid():
            edituser.first_name = form.cleaned_data['first_name']
            edituser.last_name = form.cleaned_data['last_name']
            edituser.phone = form.cleaned_data['phone']
            edituser.address = form.cleaned_data['address']
            if form.cleaned_data['image']:
                    edituser.image = form.cleaned_data['image']
            edituser.save()
            return redirect('/')

    elif request.method == 'GET':

        form = User_edit_form(initial={
                                    'user':request.user.username,  
                                    'first_name':request.user.profile.first_name, 
                                    'last_name':request.user.profile.last_name, 
                                    'phone':request.user.profile.phone, 
                                    'address':request.user.profile.address, 
                                    'image':request.user.profile.image,                                                              
                                    })
        context = {'form':form}
        
    return render(request, 'users/edit_profile.html', context=context)


def profile(request):#muestra los datos del perfil
    user_=User.objects.get(username=request.user)
    profile = User_profile.objects.filter(user_id=user_) 
    context = {
            'profile':profile
        }
    return render(request, 'users/profile.html', context=context)