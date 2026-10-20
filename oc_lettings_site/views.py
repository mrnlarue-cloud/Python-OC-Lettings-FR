"""Vues générales du site Orange County Lettings."""

from django.shortcuts import render

# ==================================================
# VUE : PAGE D'ACCUEIL
# ==================================================


def index(request):
    """Affiche la page d'accueil du site."""
    return render(request, "index.html")
