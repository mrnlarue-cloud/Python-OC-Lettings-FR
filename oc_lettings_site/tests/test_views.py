"""Tests des vues de l'application principale."""

# ==================================================
# TESTS DES VUES - PAGE D'ACCUEIL - INTEGRATION
# ==================================================


def test_affichage_accueil(client):
    """Vérification de l'accueil avec les liens principaux."""

    reponse = client.get("/")

    assert reponse.status_code == 200
    assert b"Welcome to Holiday Homes" in reponse.content
    assert b'href="/lettings/"' in reponse.content
    assert b'href="/profiles/"' in reponse.content
