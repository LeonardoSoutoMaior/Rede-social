from django.urls import path
from . import views

urlpatterns =[
    path('home/', views.home, name="home"),
    path('publicacao/', views.publicacao, name="publicacao"),
    path('adicionar_comentario/<int:publicacao_id>/', views.adicionar_comentario, name="adicionar_comentario"),
    path('comentarios/<int:publicacao_id>/', views.comentarios, name="comentarios"),
    path('adicionar_resposta_comentario/<int:comentario_id>/', views.adicionar_resposta_comentario, name="adicionar_resposta_comentario"),
    path('comentarios_do_comentario/<int:comentario_id>/', views.comentarios_do_comentario, name="comentarios_do_comentario"),
    path('curtir_publicacao/<int:publicacao_id>/', views.curtir_publicacao, name="curtir_publicacao"),
    
]