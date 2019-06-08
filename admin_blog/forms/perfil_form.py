from django.contrib.auth.forms import UserChangeForm
from ..models import Usuario

class PerfilForm(UserChangeForm):
    class Meta:
        model = Usuario
        fields = ['nome', 'email', 'pais_origem']