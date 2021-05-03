from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm

def error404_page(request, exception):

    return render(request,'404.html')

def index(request):
    return render(request,'mainapp/index.html',{
        'title':'Inicio'
    }) 

def about(request):
    return render(request, 'mainapp/about.html',{
        'title':'About us'
    })

def register_page(request):
    if request.user.is_authenticated:
        return redirect('index')

    register_form = RegisterForm(request.POST)
    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request,'Tu registro fue todo un éxito 🥳')

            return redirect('index')
        else:
            messages.warning(request,'Prueba ingresar bien los datos 😬')

    return render(request,'users/register.html',{
        'title':'Regístrate',
        'register_form': register_form
    })

def login_page(request):
    if request.user.is_authenticated:
        return redirect('index')

    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            messages.success(request,'Nos alegra verte por aquí')

            return redirect('index')
        else:
            messages.warning(request,'Los datos no son correctos')

    return render(request,'users/login.html',{
    'title':'Iniciar sessión'
    })

def logout_user(request):
    logout(request)
    return redirect('login')

