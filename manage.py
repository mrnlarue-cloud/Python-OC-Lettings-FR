"""Fichier permettant de lancer les commandes Django depuis le terminal."""

import os
import sys

# ==================================================
# FONCTION : EXECUTION DES COMMANDES DJANGO
# ==================================================


def main():
    """Exécute les commandes Django depuis le terminal."""

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "oc_lettings_site.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


# ==================================================
# LANCEMENT
# ==================================================

if __name__ == "__main__":
    main()
