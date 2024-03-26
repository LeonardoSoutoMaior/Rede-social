from django.urls import path
from . import views

urlpatterns =[
    path('home/', views.home, name="home"),
    path('publicacao/', views.publicacao, name="publicacao"),
    path('adicionar_comentario/<int:publicacao_id>/', views.adicionar_comentario, name="adicionar_comentario"),
    path('home/comentarios/<int:publicacao_id>/', views.comentarios, name="comentarios"),
    
]