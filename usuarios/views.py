from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.messages import constants
from django.contrib import messages
from django.contrib import auth


def cadastro(request):
    if request.method == 'GET':
        return render(request, 'cadastro.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')
        
        if not senha == confirmar_senha:
            messages.add_message(request, constants.ERROR, 'Senha e confirmar senha não coincidem')
            return redirect('/usuarios/cadastro')
        
        user = User.objects.filter(email=email)
        
        if user.exists():
            messages.add_message(request, constants.ERROR, 'Usuário já existe')
            return redirect('/usuarios/cadastro')
        
        try:
            User.objects.create_user(
                username=username, # o primeiro campo é o que fica no BD, pra saber tem que ver o nome na tabela auth_user
                email=email,
                password=senha
            )
            
            return redirect('/usuarios/logar')
        
        except:
            messages.add_message(request, constants.ERROR, 'Erro interno do servidor')
            return redirect('/usuarios/cadastro')
        
        
def logar(request):
    if request.method == "GET":
        return render(request, 'login.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        senha = request.POST.get('senha')
        
        user = auth.authenticate(request, username=username, password=senha) # a variável user recebe a função de autenticação do django, nisso ela recebe o valor informado pelo usuario
        
        if user:
            auth.login(request, user)
            messages.add_message(request, constants.SUCCESS, 'Logado')
            return redirect('/home/home')
        else:
            messages.add_message(request, constants.ERROR, 'Email ou senha inválidos')
            return redirect('/usuarios/logar/')
        
def logout(request):
    auth.logout(request)
    return redirect('/usuarios/logar')