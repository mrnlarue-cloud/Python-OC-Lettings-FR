"""Configuration de l'application des profils utilisateurs"""

from django.apps import AppConfig


class ProfilesConfig(AppConfig):
    """Application dédiée aux profils utilisateurs."""

    default_auto_field = "django.db.models.AutoField"
    name = "profiles"
