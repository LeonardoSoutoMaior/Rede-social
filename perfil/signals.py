from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Seguir, Perfil

@receiver(post_save, sender=Seguir)
def atualizar_numero_seguidores(sender, instance, created, **kwargs):
    if created:
        usuario_seguindo = instance.seguindo
        perfil, _ = Perfil.objects.get_or_create(usuario=usuario_seguindo)
        perfil.total_seguidores +=1
        perfil.save()
        
        usuario_seguidor = instance.seguidor
        perfil_seguidor, _ = Perfil.objects.get_or_create(usuario=usuario_seguidor)
        perfil_seguidor.total_seguindo +=1
        perfil_seguidor.save()