"""Tests des modèles de l'application profiles."""

import pytest
from django.contrib.auth.models import User
from django.db import IntegrityError

from profiles.models import Profile

# ==================================================
# TESTS DES MODELS - INTEGRATION
# ==================================================


@pytest.mark.django_db
def test_one_profile_per_user():
    """Vérification qu'un 'user' ne peut avoir qu'un profil."""

    # Création d'un 'user' dans la BD
    user = User.objects.create_user(username="utilisateur_test")

    # Enregistrement du profil 1 pour le 'user'
    Profile.objects.create(user=user, favorite_city="Los Angeles")

    # Vérification d'une erreur si tentative de créer un second profil pour le même 'user'
    with pytest.raises(IntegrityError):
        Profile.objects.create(user=user, favorite_city="San Francisco")
