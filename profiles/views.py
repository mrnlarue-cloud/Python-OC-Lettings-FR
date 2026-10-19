"""Vues de l'application profiles."""

from django.shortcuts import render
from .models import Profile

# ==================================================
# VUE : LISTE DES PROFILS
# ==================================================


def index(request):
    """Affiche la liste de profils utilisateurs."""
    profiles_list = Profile.objects.all()
    context = {"profiles_list": profiles_list}
    return render(request, "temp_profiles/index.html", context)


# ==================================================
# VUE : DETAIL D'UN PROFIL
# ==================================================


def profile(request, username):
    """Affiche les informations d'un utilisateur précis."""
    profile = Profile.objects.get(user__username=username)
    context = {"profile": profile}
    return render(request, "temp_profiles/profile.html", context)
