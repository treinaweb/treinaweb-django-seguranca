from django.shortcuts import render, redirect
from admin_blog.services import post_service, comentario_service, usuario_service
from admin_blog.forms import comentario_form, usuario_form, login_form, perfil_form
from admin_blog.entidades.comentario import Comentario
from admin_blog.entidades.usuario import Usuario
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    posts = post_service.listar_posts()
    return render(request, 'blog/index.html', {'posts': posts})

def listar_post_id(request, id):
    post = post_service.listar_post_id(id)
    comentarios = comentario_service.listar_comentarios(id)
    if request.method == "POST":
        if request.user.is_authenticated:
            form_comentario = comentario_form.ComentarioForm(request.POST)
            if form_comentario.is_valid():
                conteudo = form_comentario.cleaned_data["conteudo"]
                usuario = request.user
                comentario_novo = Comentario(conteudo=conteudo, post=post, usuario=usuario)
                comentario_service.cadastrar_comentario(comentario_novo)
                return redirect('listar_post', post.id)
        else:
            return redirect('logar_usuario')
    else:
        form_comentario = comentario_form.ComentarioForm()
    return render(request, 'blog/post.html', {'post': post, 'comentarios': comentarios, 'form_comentario': form_comentario})

def cadastrar_usuario(request):
    if request.method == "POST":
        form_usuario = usuario_form.UsuarioForm(data=request.POST)
        if form_usuario.is_valid():
            nome = form_usuario.cleaned_data["nome"]
            email = form_usuario.cleaned_data["email"]
            pais_origem = form_usuario.cleaned_data["pais_origem"]
            password = form_usuario.cleaned_data["password1"]
            usuario_novo = Usuario(nome=nome, email=email, pais_origem=pais_origem, password=password)
            usuario_service.cadastrar_usuario(usuario_novo)
            return redirect('home')
    else:
        form_usuario = usuario_form.UsuarioForm()
    return render(request, 'usuario/cadastro.html', {'form_usuario': form_usuario})

def logar_usuario(request):
    if request.method == "POST":
        form_login = login_form.LoginForm(data=request.POST)
        if form_login.is_valid():
            username = form_login.cleaned_data["username"]
            password = form_login.cleaned_data["password"]
            usuario = authenticate(request, username=username, password=password)
            if usuario is not None:
                login(request, usuario)
                return redirect('home')
            else:
                form_login = login_form.LoginForm()
    else:
        form_login = login_form.LoginForm()
    return render(request, 'usuario/login.html', {'form_login': form_login})

def deslogar_usuario(request):
    logout(request)
    return redirect('home')

@login_required()
def perfil_usuario(request):
    if request.method == "POST":
        form_usuario = perfil_form.PerfilForm(request.POST, instance=request.user)
        if form_usuario.is_valid():
            form_usuario.save()
            return redirect('home')
    else:
        form_usuario = perfil_form.PerfilForm(instance=request.user)
    return render(request, 'usuario/perfil.html', {'form_usuario': form_usuario})

@login_required()
def alterar_senha(request):
    if request.method == "POST":
        form_senha = PasswordChangeForm(request.user, request.POST)
        if form_senha.is_valid():
            user = form_senha.save()
            update_session_auth_hash(request, user)
            return redirect('home')
    else:
        form_senha = PasswordChangeForm(request.user)
    return render(request, 'usuario/alterar_senha.html', {'form_senha': form_senha})