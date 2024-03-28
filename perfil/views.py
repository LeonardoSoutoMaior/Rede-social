from django.shortcuts import get_object_or_404, render, redirect
from .models import Perfil, Seguir
from home.models import Publicacao
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse


def renderizar_perfil(request):
    publicacoes = Publicacao.objects.filter(autor=request.user)
    
    seguindo = Seguir.objects.filter(seguidor=request.user).count()
    
    seguidores = Seguir.objects.filter(seguindo=request.user).count()
    
    return render(request, 'perfil.html', {'publicacoes': publicacoes,
                  'seguindo': seguindo,
                  'seguidores': seguidores})


@login_required
def seguir_usuario(request, usuario_id):
    perfil_a_seguir = get_object_or_404(Perfil, id=usuario_id)
    perfil_usuario = request.user.perfil
    
    seguindo = Seguir.objects.filter(seguidor=perfil_usuario, seguindo=perfil_a_seguir).exists()
    
    if seguindo:
        Seguir.objects.filter(seguidor=perfil_usuario, seguindo=perfil_a_seguir).delete()
        seguido = False
    else:
        Seguir.objects.create(seguidor=perfil_usuario, seguindo=perfil_a_seguir)
        seguido = True
        
    return JsonResponse({'seguindo': seguido})