from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('post/<int:id>', listar_post_id, name='listar_post'),
    path('cadastrar_usuario/', cadastrar_usuario, name='cadastrar_usuario'),
    path('logar_usuario/', logar_usuario, name='logar_usuario'),
    path('deslogar_usuario/', deslogar_usuario, name='deslogar_usuario'),
    path('alterar_senha/', alterar_senha, name='alterar_senha'),
    path('perfil_usuario/', perfil_usuario, name='perfil_usuario'),
]