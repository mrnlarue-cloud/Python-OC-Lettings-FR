"""Tests des modèles de l'application lettings."""

import pytest
from django.core.exceptions import ValidationError

from lettings.models import Address, Letting

# ==================================================
# TESTS UNITAIRES - ADDRESS
# ==================================================


def test_address_number():
    """Vérifie la limite maximale du numéro d'adresse."""
    field = Address._meta.get_field("number")

    # Exemple de valeur valide
    field.clean(9999, None)

    # Exemple valeur invalide
    with pytest.raises(ValidationError):
        field.clean(10000, None)


def test_address_state():
    """Vérifie que le code d'Etat contient deux caractères"""
    field = Address._meta.get_field("state")

    # Exemple de valeur valide
    field.clean("CA", None)

    # Exemple de valeur trop courte
    with pytest.raises(ValidationError):
        field.clean("C", None)

    # Exemple de valeur trop longue
    with pytest.raises(ValidationError):
        field.clean("CAL", None)


def test_address_zip_code():
    """Vérifie la longueur max du code postal."""
    field = Address._meta.get_field("zip_code")

    # Exemple de valeur valide
    field.clean(9999, None)

    # Exemple de valeur invalide
    with pytest.raises(ValidationError):
        field.clean(100000, None)


def test_address_country_iso_code():
    """Vérification code pays à trois caractères."""
    field = Address._meta.get_field("country_iso_code")

    # Exemple de valeur valide
    field.clean("USA", None)

    # Exemple de valeur trop courte
    with pytest.raises(ValidationError):
        field.clean("US", None)

    # Exemple de valeur trop longue
    with pytest.raises(ValidationError):
        field.clean("USAA", None)


# ==================================================
# TESTS D'INTEGRATION
# ==================================================


@pytest.mark.django_db
def test_letting_address_relation():
    """Vérifie qu'une adresse est liée à une location et inversement."""
    address = Address.objects.create(
        number=123,
        street="Main Street",
        city="Los Angeles",
        state="CA",
        zip_code=9999,
        country_iso_code="USA",
    )

    letting = Letting.objects.create(
        title="Appartement de test",
        address=address,
    )

    # Récupère la location depuis la BD
    letting_saved = Letting.objects.get(pk=letting.pk)

    # Vérification de la bonne association
    assert letting_saved.address == address

    # Vérification de la relation inverse
    address_saved = Address.objects.get(pk=address.pk)
    assert address_saved.letting == letting_saved


@pytest.mark.django_db
def test_letting_deleted_address():
    """Vérifie que la suppression d'une adresse supprime la location."""
    address = Address.objects.create(
        number=123,
        street="Main Street",
        city="Los Angeles",
        state="CA",
        zip_code=9999,
        country_iso_code="USA",
    )

    letting = Letting.objects.create(
        title="Appartement de test",
        address=address,
    )

    address.delete()

    assert not Letting.objects.filter(pk=letting.pk).exists()
