"""Tests des URLS de l'application Lettings."""

from django.urls import resolve
from lettings import views

# ==================================================
# TESTS DES URL - DETAIL D'UNE LOCATION
# ==================================================


def test_url_letting_detail():
    """Vérification du routage vers une location spécifique."""

    # Demande à Django la vue correspondant à l'adresse /lettings/123/
    correspondance = resolve("/lettings/123/")

    # Vérification que l'adresse mène vers la fonction letting()
    assert correspondance.func == views.letting

    # Vérifie que Django récupère le num 123 comme ID d la location
    assert correspondance.kwargs == {"letting_id": 123}

    # Vérifie le bon nom d'adresse
    assert correspondance.view_name == "lettings:letting"
