from django import forms
from ..models import Post, Categoria
from upload_validator import FileTypeValidator

class PostForm(forms.ModelForm):
    categoria = forms.ModelChoiceField(queryset=Categoria.objects.all())
    capa = forms.ImageField(
        validators=[FileTypeValidator(
            allowed_types=['image/jpeg']
        )]
    )
    class Meta:
        model = Post
        fields = ['titulo', 'descricao', 'conteudo', 'categoria', 'capa']