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

    # Vérification que Django construit la bonne adresse
    assert adresse == "/profiles/bobby_test/"

    # Vérification que l'adresse amène à la bonne fonction
    correspondance = resolve(adresse)
    assert correspondance.func == views.profile

    # Vérification de la transmission du bon 'user'
    assert correspondance.kwargs == {"username": "bobby_test"}


# ==================================================
# TESTS DES URL - LISTE DES PROFILS INTEGRATION
# ==================================================


def test_liste_url_profils():
    """Vérifie que l'URL dirige vers la liste de tous les profils."""

    # Construction de l'adresse de la liste des profils par Django
    adresse = reverse("profiles:index")

    # Vérification de la bonne construction d'adresse par Django
    assert adresse == "/profiles/"

    # Vérification de l'adresse avec la fonction index()
    correspondance = resolve(adresse)
    assert correspondance.func == views.index
