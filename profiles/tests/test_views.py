"""Tests des vues de l'application Profiles."""

import pytest
from django.contrib.auth.models import User

from profiles.models import Profile

# ==================================================
# TESTS DES VUES - AFFICHAGE ERREUR 404 - INTEGRATION
# ==================================================


@pytest.mark.django_db
def test_profile_inexistant(client):
    """Un profil inexistant doit renvoyer à une erreur 404."""

    # Demande d'affichage d'un profil inexistant en DB
    reponse = client.get("/profiles/utilisateur_inexistant/")

    # Vérification que django ne renvoie pas une erreur 500
    assert reponse.status_code == 404


# ==================================================
# TESTS DES VUES - AFFICHAGE DU BON PROFIL - INTEGRATION
# ==================================================


@pytest.mark.django_db
def test_affichage_profil_demande(client):
    """Vérifie que les infos appartiennent au bon 'User'."""

    # Création de deux 'users' test en DB
    pamela = User.objects.create_user(
        username="pamela_test",
        first_name="Pamela",
        email="pamela@example.com",
    )

    bobby = User.objects.create_user(
        username="bobby_test",
        first_name="Bobby",
        email="bobby@example.com",
    )

    # Création d'un profil 'user' pour chacun
    Profile.objects.create(user=pamela, favorite_city="Laguna Woods")
    Profile.objects.create(user=bobby, favorite_city="Laguna Hills")

    # Affichage du profil de Bobby
    reponse = client.get("/profiles/bobby_test/")
    contenu = reponse.content.decode()

    # Vérification des infos de Bobby
    assert reponse.status_code == 200
    assert "bobby@example.com" in contenu
    assert "Laguna Hills" in contenu

    # Vérifie que les infos de Pamela ne soient pas affichées
    assert "pamela@example.com" not in contenu
    assert "Laguna Woods" not in contenu
