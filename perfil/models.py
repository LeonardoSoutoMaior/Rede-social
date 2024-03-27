from django.db import models
from django.contrib.auth.models import User


class Seguir(models.Model):
    seguidor = models.ForeignKey(User, related_name='seguidores', on_delete=models.CASCADE)
    seguindo = models.ForeignKey(User, related_name='seguindo', on_delete=models.CASCADE)
    data_seguimento = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.seguidor.username} segue {self.seguindo.username}'
    
class Perfil(models.Model):
    usuario = models.OneToOneField(User, related_name='perfil', on_delete=models.CASCADE)
    total_seguidores = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return f'Perfil de {self.usuario.username}'