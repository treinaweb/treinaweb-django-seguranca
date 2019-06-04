from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .manager import UsuarioManager

# Create your models here.

class Usuario(AbstractBaseUser):
    objects = UsuarioManager()

    nome = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(unique=True, null=False, blank=False)
    pais_origem = models.CharField(max_length=20, null=False, blank=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nome', 'pais_origem']

    def __str__(self):
        return self.email

class Categoria(models.Model):
    nome = models.CharField(max_length=30, null=False, blank=False)
    descricao = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.nome

class Post(models.Model):
    titulo = models.CharField(max_length=100, null=False, blank=False)
    descricao = models.CharField(max_length=200, null=False, blank=False)
    conteudo = models.TextField(blank=False, null=False)
    categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE)
    data_cadastro = models.DateField(auto_now_add=True)
    data_edicao = models.DateField(auto_now=True)

    def __str__(self):
        return self.titulo

class Comentario(models.Model):
    conteudo = models.TextField(null=False, blank=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.conteudo