from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from users.forms import User_registration_form
from django.http import HttpResponse
from users.models import User_profile

def login_request(request):
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




def register(request):
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



def show_profile(request):
    if request.user.is_authenticated:
        return HttpResponse(request.user.profile.image.url)

# poner login request que solo el usuario pueda verve su propio perfil y armar bien el template 
#no anda 
def profile(request, pk):
    if request.method == 'GET':
        profile = User_profile.objects.get(pk=pk)
        context = {'profile':profile}
        return render(request, 'users/profile.html', context=context)
        #para cuando use el boton buy o add to cart
    elif request.method == 'POST':
        profile = User_profile.objects.get(pk=pk)
        return redirect('General/index.html')
