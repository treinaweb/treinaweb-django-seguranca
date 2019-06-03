from django.shortcuts import render, redirect
from admin_blog.services import post_service, comentario_service
from admin_blog.forms import comentario_form
from admin_blog.entidades.comentario import Comentario

# Create your views here.

def index(request):
    posts = post_service.listar_posts()
    return render(request, 'blog/index.html', {'posts': posts})

def listar_post_id(request, id):
    post = post_service.listar_post_id(id)
    comentarios = comentario_service.listar_comentarios(id)
    if request.method == "POST":
        form_comentario = comentario_form.ComentarioForm(request.POST)
        if form_comentario.is_valid():
            conteudo = form_comentario.cleaned_data["conteudo"]
            comentario_novo = Comentario(conteudo=conteudo, post=post)
            comentario_service.cadastrar_comentario(comentario_novo)
            return redirect('listar_post', post.id)
    else:
        form_comentario = comentario_form.ComentarioForm()
    return render(request, 'blog/post.html', {'post': post, 'comentarios': comentarios, 'form_comentario': form_comentario})
