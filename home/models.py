from django.db import models
from django.contrib.auth.models import User


class Publicacao(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    conteudo = models.TextField()
    data_publicacao = models.DateTimeField(auto_now_add=True)
    curtidas = models.ManyToManyField(User, related_name='curtidas', blank=True)
    
    def total_curtidas(self):
        return self.curtidas.count()
    
    def __str__(self):
        return f'{self.autor.username} Publicação: {self.conteudo}'
    
class Comentario(models.Model):
    publicacao = models.ForeignKey(Publicacao, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    texto = models.TextField()
    data_comentario = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'Comentario de {self.usuario.username} Comentario: {self.publicacao.conteudo}'
    

class RespostaComentario(models.Model):
    comentario = models.ForeignKey(Comentario, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    texto = models.TextField()
    data_resposta = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'Resposta de {self.usuario.username} Comentario: {self.comentario.publicacao.conteudo}'
    