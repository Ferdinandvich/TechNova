from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.

def home(request):
    return render(request, 'home.html')

def produtos(request):
    return render(request, 'produtos.html')

def sobre(request):
    return render(request, 'sobre.html')

def contato(request):
    return render(request, 'contato.html')

def registrarUsuario(request):
    if request.method == 'POST':
        nome_usuario = request.POST.get('usuario')
        senha = request.POST.get('senha')
        user = User.objects.create_user(username=nome_usuario, password=senha)
        user.save()
    return render(request, 'registrar-usuario.html')

def custom_logout(request):
    logout(request)
    return render(request, 'logout.html')

def login(request):
    return render(request, 'login.html')