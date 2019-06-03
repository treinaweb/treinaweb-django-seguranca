from django.urls import path
from .views import *

urlpatterns = [
    path('listar_posts/', listar_posts, name='listar_posts'),
    path('editar_post/<int:id>', editar_post, name='editar_post'),
    path('remover_post/<int:id>', remover_post, name='remover_post'),
    path('cadastrar_post/', cadastrar_post, name='cadastrar_post'),

]