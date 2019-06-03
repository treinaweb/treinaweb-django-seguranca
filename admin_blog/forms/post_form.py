from django import forms
from ..models import Post, Categoria

class PostForm(forms.ModelForm):
    categoria = forms.ModelChoiceField(queryset=Categoria.objects.all())
    class Meta:
        model = Post
        fields = ['titulo', 'descricao', 'conteudo', 'categoria']