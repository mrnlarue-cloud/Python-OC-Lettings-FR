"""Modèles des profils utilisateurs."""

from django.db import models
from django.contrib.auth.models import User

# ==================================================
# MODÈLE : PROFILE (utilisateur)
# ==================================================


class Profile(models.Model):
    """Représente le profil d'un utilisateur."""

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        """Retourne le nom de l'utilisateur."""
        return self.user.username
