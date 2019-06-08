from .models import Usuario

def save_profile(backend, user, details, response, *args, **kwargs):
    if backend.name == "google-oauth2":
        profile = user
        if profile is None:
            profile = Usuario(user_id=user.id)
        profile.nome = details['fullname']
        profile.save()