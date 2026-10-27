"""Tests des vues de l'application lettings."""

import pytest

# ==================================================
# TESTS DES VUES - ERREUR 404
# ==================================================


@pytest.mark.django_db
def test_letting_inexistant_404(client):
    """Vérifie qu'une location qui n'existe pas renvoie un page 404."""

    reponse = client.get("/lettings/999999/")

    assert reponse.status_code == 404
