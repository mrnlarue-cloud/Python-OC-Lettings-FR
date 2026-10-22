"""Configuration de l'application des locations."""

from django.apps import AppConfig


class LettingsConfig(AppConfig):
    """Application dédiée à la partie location du projet Django."""

    default_auto_field = "django.db.models.AutoField"
    name = "lettings"
