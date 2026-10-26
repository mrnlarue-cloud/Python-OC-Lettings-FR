"""Tests des modèles de l'application lettings."""

import pytest
from django.core.exceptions import ValidationError

from lettings.models import Address

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
