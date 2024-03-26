from django.contrib import admin
from .models import Publicacao, Comentario, RespostaComentario

admin.site.register(Publicacao)
admin.site.register(Comentario)
admin.site.register(RespostaComentario)
