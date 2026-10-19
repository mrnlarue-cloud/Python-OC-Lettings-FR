"""Vues de l'application lettings."""

from django.shortcuts import render
from .models import Letting

# ==================================================
# VUE : LISTE DES LOCATIONS
# ==================================================


def index(request):
    """Affiche la liste des locations."""
    lettings_list = Letting.objects.all()
    context = {"lettings_list": lettings_list}
    return render(request, "lettings_index.html", context)


# ==================================================
# VUE : DETAIL D'UNE LOCATION
# ==================================================


def letting(request, letting_id):
    """Affiche les informations d'une location précise."""
    letting = Letting.objects.get(id=letting_id)
    context = {
        "title": letting.title,
        "address": letting.address,
    }
    return render(request, "letting.html", context)
