"""Tests des vues de l'application lettings."""

import pytest
from lettings.models import Letting, Address

# ==================================================
# TESTS DES VUES - ERREUR 404 - INTEGRATION
# ==================================================


@pytest.mark.django_db
def test_letting_inexistant_404(client):
    """Vérifie qu'une location qui n'existe pas renvoie une page 404."""

    # Exemple de requête vers une location inexistante en BD
    reponse = client.get("/lettings/999999/")

    # Vérifie que Django renvoie une erreur 404 et non 500 (serveur)
    assert reponse.status_code == 404


# ==================================================
# TESTS DES VUES - DETAIL D'UNE LOCATION - INTEGRATION
# ==================================================


@pytest.mark.django_db
def test_letting_detail(client):
    """Vérifie l'affichage des infos d'une location"""

    # Données de test
    address = Address.objects.create(
        number=123,
        street="Main Street",
        city="Los Angeles",
        state="CA",
        zip_code=9999,
        country_iso_code="USA",
    )

    letting = Letting.objects.create(
        title="Appartement Test",
        address=address,
    )

    # Accès à la page de location avec id primary key
    reponse = client.get(f"/lettings/{letting.pk}/")
    # Conversion du html en texte pour vérifier les infos affichées
    contenu = reponse.content.decode()

    # Vérification du succès de la requête
    assert reponse.status_code == 200
    assert "Appartement Test" in contenu
    assert "123 Main Street" in contenu


# ==================================================
# TESTS DES VUES - LISTE DES LOCATIONS - INTEGRATION
# ==================================================


@pytest.mark.django_db
def test_lettings_listen(client):
    """Vérifie l'affichage d'une location dans la liste."""

    # Création d'une location et de son adresse en BD
    address = Address.objects.create(
        number=123,
        street="Main Street",
        city="Los Angeles",
        state="CA",
        zip_code=9999,
        country_iso_code="USA",
    )

    # Création de la location associée à l'adresse
    letting = Letting.objects.create(
        title="Appartement Test",
        address=address,
    )

    # Simulation d'une visite sur la liste des locations
    reponse = client.get("/lettings/")
    contenu = reponse.content.decode()

    # Vérifie que la page fonctionne et affiche la location
    assert reponse.status_code == 200
    assert "Appartement Test" in contenu

    # Vérifie que lien dirige vers la location voulue
    assert f'href="/lettings/{letting.pk}/"' in contenu
