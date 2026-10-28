"""Tests des vues de l'application Profiles."""

import pytest

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
