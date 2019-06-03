from django.shortcuts import render, redirect
from admin_blog.services import post_service, comentario_service
from admin_blog.forms import comentario_form
from admin_blog.entidades.comentario import Comentario
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django.contrib.auth import authenticate, login

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

def cadastrar_usuario(request):
    if request.method == "POST":
        form_usuario = UserCreationForm(request.POST)
        if form_usuario.is_valid():
            form_usuario.save()
            return redirect('home')
    else:
        form_usuario = UserCreationForm()
    return render(request, 'usuario/cadastro.html', {'form_usuario': form_usuario})

def logar_usuario(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        usuario = authenticate(request, username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('home')
        else:
            form_login = AuthenticationForm()
    else:
        form_login = AuthenticationForm()
    return render(request, 'usuario/login.html', {'form_login': form_login})