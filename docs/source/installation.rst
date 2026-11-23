=========================
Installation et démarrage
=========================

------------------------------------------
Présentation
------------------------------------------

Voici la partie de la documentation qui permet d'expliquer comment installer l'application ORANGE COUNTY LETTINGS sur n'importe quel ordinateur. De même, c'est aussi ce qui donne la ligne à suivre pour lancer cette application en local dans un environnement dédié.

------------------------------------------
Les prérequis
------------------------------------------

Avant de débuter sur l'application ORANGE COUNTY LETTINGS, il nous faut disposer des outils suivants :

* Python 3.11
* Git

Le fichier ``requirements.txt`` vient répertorier les dépendances nécessaires à l'application.


------------------------------------------
La récupération du projet
------------------------------------------

Le code source est disponible sur `GitHub <https://github.com/mrnlarue-cloud/Python-OC-Lettings-FR>`_.

Cloner le dépôt :

.. code-block:: powershell

   git clone https://github.com/mrnlarue-cloud/Python-OC-Lettings-FR.git

Accéder au répertoire du projet :

.. code-block:: powershell

   cd Python-OC-Lettings-FR


------------------------------------------
Installation des dépendances
------------------------------------------

Il nous faut créer et activer un environnement virtuel :

.. code-block:: powershell

   python -m venv .venv
   .\.venv\Scripts\Activate.ps1

Et ensuite, installer les dépendances :

.. code-block:: powershell

   python -m pip install -r requirements.txt


------------------------------------------
Configuration de l'environnement
------------------------------------------

Les variables d'environnement sont définies dans un fichier de type ``.env``. Comme elles ne sont pas à partager, il faut créer votre propre fichier à partir du modèle fourni :

.. code-block:: powershell

   Copy-Item .env.exemple .env

Renseignement des variables nécessaires :

* ``DJANGO_SECRET_KEY`` : la clé secrète Django.
* ``DJANGO_DEBUG`` : mode débogage.
* ``DJANGO_ALLOWED_HOSTS`` : hôtes autorisés.

Pour le développement en local, définir ``DJANGO_DEBUG=True`` et autoriser ``localhost,127.0.0.1``.

Encore une fois, le fichier ``.env`` ne doit surtout pas être publié sur GitHub.


------------------------------------------
Base de données
------------------------------------------

Ici, une particularité : comme l'application utilise SQLite en développement local et PostgreSQL en production, en l'absence de variable ``DATABASE_URL``, Django utilisera automatiquement la base SQLite locale.

Il faudra alors appliquer des migrations :

.. code-block:: powershell

   python manage.py migrate

Ces migrations vont créer les tables nécessaires, mais ne chargeront pas automatiquement les données de démonstration.


------------------------------------------
Démarrage de l'application
------------------------------------------

Pour le démarrage du serveur Django :

.. code-block:: powershell

   python manage.py runserver

Le site ORANGE COUNTY LETTINGS est accessible à l'adresse :

http://127.0.0.1:8000/

Les locations immobilières et les profils utilisateurs sont accessibles depuis la page d'accueil.


------------------------------------------
Administration
------------------------------------------

L'interface administrateur est disponible à l'URL :

http://127.0.0.1:8000/admin/

Si nécessaire, pour la création d'un compte administrateur :

.. code-block:: powershell

   python manage.py createsuperuser


------------------------------------------
Tests et qualité du code
------------------------------------------

Exécution des tests avec Pytest :

.. code-block:: powershell

   python -m pytest

Vérification de la qualité du code avec Flake8 :

.. code-block:: powershell

   python -m flake8 --extend-exclude=.venv

Ces contrôles permettent de vérifier le fonctionnement de l'application avant le déploiement.