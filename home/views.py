from django.utils import timezone
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.messages import constants
from django.contrib import messages
from django.contrib import auth
from home.models import Publicacao, Comentario, RespostaComentario
from django.shortcuts import render, get_object_or_404

def home(request):
    if not request.user.is_authenticated:
        return render(request, '/usuarios/logar')
    else:
        publicacoes = Publicacao.objects.all()
        return render(request, 'home.html', {'publicacoes': publicacoes})


    
def publicacao(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            conteudo = request.POST.get('post-text')
            if conteudo.strip():
                nova_publicacao = Publicacao(autor=request.user, conteudo=conteudo, data_publicacao=timezone.now())
                nova_publicacao.save()
            return redirect('home')
    

def adicionar_comentario(request, publicacao_id): # Esse publicacao_id foi passado na urls.py
    if request.method == 'POST':
        if request.user.is_authenticated:
            texto = request.POST.get('comment-text')
            if texto.strip():
                publicacao = Publicacao.objects.get(pk=publicacao_id)
                novo_comentario = Comentario(usuario=request.user, publicacao=publicacao, texto=texto, data_comentario=timezone.now())
                novo_comentario.save()
        return redirect('comentarios', publicacao_id=publicacao_id) # Aqui redireciona para a view comentarios
    

def comentarios(request, publicacao_id):
    publicacao = get_object_or_404(Publicacao, pk=publicacao_id)
    comentarios = Comentario.objects.filter(publicacao=publicacao)
    return render(request, 'detalhes_publicacao.html', {'publicacao': publicacao,
                                                        'comentarios': comentarios})
    
    
def adicionar_resposta_comentario(request, comentario_id):
    if request.method == 'POST':
        if request.user.is_authenticated:
            texto_resposta = request.POST.get('texto-resposta')
            if texto_resposta.strip():
                comentario = Comentario.objects.get(pk=comentario_id)
                nova_resposta = RespostaComentario(comentario=comentario, usuario=request.user, texto=texto_resposta, data_resposta=timezone.now())
                nova_resposta.save()
        
        return redirect('comentarios_do_comentario', comentario_id=comentario_id)
    
    
def comentarios_do_comentario(request, comentario_id):
    comentario_pai = get_object_or_404(Comentario, pk=comentario_id)
    comentarios_do_comentario = RespostaComentario.objects.filter(comentario=comentario_pai)
    return render(request, 'detalhes_comentario.html', {'comentario_pai':comentario_pai,
                                                        'comentarios_do_comentario': comentarios_do_comentario})

