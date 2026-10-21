"""Suppression des anciens modèles après transfert des données."""

from django.db import migrations

# ==================================================
# MIGRATION : SUPPRESSION DES ANCIENS MODÈLES
# ==================================================


class Migration(migrations.Migration):
    """Supprime les anciens modèles après leurs migrations de données."""

    dependencies = [
        ("oc_lettings_site", "0001_initial"),
        ("lettings", "0002_transfert_donnees"),
        ("profiles", "0002_transfert_donnees"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="letting",
            name="address",
        ),
        migrations.RemoveField(
            model_name="profile",
            name="user",
        ),
        migrations.DeleteModel(
            name="Address",
        ),
        migrations.DeleteModel(
            name="Letting",
        ),
        migrations.DeleteModel(
            name="Profile",
        ),
    ]
