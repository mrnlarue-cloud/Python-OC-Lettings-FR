"""Tests des URLs de l'application Profiles."""

from django.urls import resolve, reverse
from profiles import views

# ==================================================
# TESTS DES URL - PROFIL UTILISATEUR - INTEGRATION
# ==================================================


def test_url_profile():
    """Vérifie que l'URL accède au profil souhaité."""

    # Demande de construction de l'adresse du profil de Bobby à Django
    adresse = reverse(
        "profiles:profile",
        kwargs={"username": "bobby_test"},
    )

    # Vérification que Django crée la bonne adresse
    correspondance = resolve(adresse)

    # Vérification que l'adresse amène à la bonne fonction
    assert correspondance.func == views.profile

    # Vérification de la transmission du bon 'user'
    assert correspondance.kwargs == {"username": "bobby_test"}
