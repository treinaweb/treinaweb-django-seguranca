from django.shortcuts import render, redirect
from .services import post_service
from .forms import post_form
from .entidades.post import Post
# Create your views here.

def listar_posts(request):
    posts = post_service.listar_posts()
    return render(request, 'admin_blog/posts.html', {'posts': posts})

def cadastrar_post(request):
    if request.method == "POST":
        form_post = post_form.PostForm(request.POST)
        if form_post.is_valid():
            titulo = form_post.cleaned_data["titulo"]
            descricao = form_post.cleaned_data["descricao"]
            conteudo = form_post.cleaned_data["conteudo"]
            categoria = form_post.cleaned_data["categoria"]
            post_novo = Post(titulo=titulo, descricao=descricao, conteudo=conteudo, categoria=categoria)
            post_service.cadastrar_post(post_novo)
            return redirect('home')
    else:
        form_post = post_form.PostForm()
    return render(request, 'admin_blog/form.html', {'form_post': form_post})

def editar_post(request, id):
    post_antigo = post_service.listar_post_id(id)
    form_post = post_form.PostForm(request.POST or None, instance=post_antigo)
    if request.method == "POST":
        if form_post.is_valid():
            titulo = form_post.cleaned_data["titulo"]
            descricao = form_post.cleaned_data["descricao"]
            conteudo = form_post.cleaned_data["conteudo"]
            categoria = form_post.cleaned_data["categoria"]
            post_novo = Post(titulo=titulo, descricao=descricao, conteudo=conteudo, categoria=categoria)
            post_service.editar_post(post_antigo, post_novo)
            return redirect('home')
    return render(request, 'admin_blog/form.html', {'form_post': form_post})

def remover_post(request, id):
    post = post_service.listar_post_id(id)
    if request.method == "POST":
        post_service.remover_post(post)
    return render(request, 'admin_blog/confirmar_exclusao.html', {'post': post})
