from django.urls import path
from . import views

urlpatterns = [
    path('seguir/<int:perfil_id>/', views.seguir_usuario, name='seguir_usuario'),
    path('perfil/', views.renderizar_perfil, name="renderizar_perfil"),
    
    
]