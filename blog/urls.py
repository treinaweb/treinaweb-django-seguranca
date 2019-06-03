from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('post/<int:id>', listar_post_id, name='listar_post'),
    path('cadastrar_usuario/', cadastrar_usuario, name='cadastrar_usuario'),
]