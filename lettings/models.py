"""Modèles des locations et de leurs adresses."""

from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator

# ==================================================
# MODELE : ADDRESS
# ==================================================


class Address(models.Model):
    """Représente l'adresse d'une location."""

    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(
        max_length=3, validators=[MinLengthValidator(3)]
    )

    class Meta:
        """Définit les options d'affichage du modèle."""

        verbose_name_plural = "Addresses"

    def __str__(self):
        """Retourne le numéro et le nom de la rue."""
        return f"{self.number} {self.street}"


# ==================================================
# MODELE : LETTING (location immobilière)
# ==================================================


class Letting(models.Model):
    """Représente une location immobilière."""

    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        """Retourne le titre de la location."""
        return self.title
