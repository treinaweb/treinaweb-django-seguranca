from ..models import *

def listar_posts():
    posts = Post.objects.all()
    return posts

def listar_post_id(id):
    post = Post.objects.get(id=id)
    return post

def cadastrar_post(post):
    Post.objects.create(titulo=post.titulo, descricao=post.descricao, conteudo=post.conteudo,
                        categoria=post.categoria)

def editar_post(post, post_novo):
    post.titulo = post_novo.titulo
    post.descricao = post_novo.descricao
    post.conteudo = post_novo.conteudo
    post.categoria = post_novo.categoria
    post.save(force_update=True)

def remover_post(post):
    post.delete()
