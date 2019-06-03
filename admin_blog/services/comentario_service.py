from ..models import *


def cadastrar_comentario(comentario):
    Comentario.objects.create(conteudo=comentario.conteudo, post=comentario.post)

def listar_comentarios(post_id):
    comentarios = Comentario.objects.filter(post__id=post_id)
    return comentarios