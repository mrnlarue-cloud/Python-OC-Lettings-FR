============================================
Le déploiement et la surveillance
============================================
--------------------------------------------
Docker
--------------------------------------------
Tout d'abord, l'application ORANGE COUNTY LETTINGS utilise Docker pour son déploiement. Le ``Dockerfile`` utilise Python 3.11, avec Gunicorn comme serveur et WhiteNoise pour les fichiers statiques.

La construction locale de l'image se fait avec :

.. code-block:: powershell

   docker build -t oc-lettings:local .

Le conteneur vient exécuter automatiquement ``collectstatic`` avant de démarrer Gunicorn sur le port 8000 (par défaut).

--------------------------------------------
Docker Hub
--------------------------------------------
Pour cette étape, GitHub Actions vient publier les images Docker sur Docker Hub.

Chaque image possède deux "tags" :

* ``latest`` : pour la dernière image publiée.
* ``SHA du commit`` : pour une version correspondant à un commit GitHub précis.

Pour récupérer l'image :

.. code-block:: powershell

   docker pull marionlarue/oc-lettings:latest

Pour le lancement du conteneur en local avec la base SQLite, depuis la racine du projet :

.. code-block:: powershell

   docker run --rm -p 8000:8000 --env-file .env -v "${PWD}/oc-lettings-site.sqlite3:/app/oc-lettings-site.sqlite3" marionlarue/oc-lettings:latest

Attention, pour que cela fonctionne, il faut que le fichier ``.env`` soit configuré et que la base SQLite locale existe déjà.

Le site est ensuite accessible sur :

http://127.0.0.1:8000/

--------------------------------------------
Pipeline CI/CD
--------------------------------------------
Concernant le pipeline CI/CD, il est configuré dans ``.github/workflows/ci.yml`` et utilise GitHub Actions.

Il fonctionne en plusieurs étapes :

* Installation de Python 3.11 et de ses dépendances.
* Vérification du code avec Flake8.
* Exécution des tests Pytest.
* Vérification d'une couverture supérieure à 80 %.
* Construction avec publication de l'image sur Docker Hub.
* Déclenchement du déploiement sur Render.

Les vérifications sont exécutées lors des "pushs" et des "pull requests".

La publication Docker et le déploiement sont réservés aux pushs sur la branche ``master``, après validation des tests.

Le pipeline est consultable sur `GitHub Actions <https://github.com/mrnlarue-cloud/Python-OC-Lettings-FR/actions>`_.

--------------------------------------------
Configuration GitHub
--------------------------------------------
Le pipeline vient utiliser une variable GitHub :

* ``DOCKERHUB_USERNAME`` : identifiant Docker Hub.

Et deux secrets GitHub :

* ``DOCKERHUB_TOKEN`` : jeton d'authentification Docker Hub.
* ``RENDER_DEPLOY_HOOK`` : URL permettant de déclencher le déploiement sur Render.

Ces informations sont configurées dans les paramètres du dépôt sur GitHub et ne doivent pas apparaître directement dans le code.

--------------------------------------------
Le déploiement sur Render
--------------------------------------------
L'application est hébergée sur Render à partir de l'image Docker publiée sur Docker Hub.

Le service web Render utilise les variables d'environnement suivantes :

* ``DJANGO_SECRET_KEY`` : clé secrète Django.
* ``DJANGO_DEBUG`` : désactivé en production.
* ``DJANGO_ALLOWED_HOSTS`` : nom de domaine autorisé.
* ``DATABASE_URL`` : connexion à PostgreSQL.
* ``SENTRY_DSN`` : connexion à Sentry.

Pour reproduire le déploiement, il faut créer un service web Docker sur Render, lui associer l'image Docker Hub et configurer ces variables. Attention, une base PostgreSQL doit également être créée et reliée au service avec ``DATABASE_URL``.

Les migrations doivent être appliquées à cette base pour que cela fonctionne :

.. code-block:: powershell

   python manage.py migrate

Cette commande doit être exécutée dans un environnement configuré pour accéder à la base PostgreSQL concernée. Le déploiement automatique utilise le "Deploy Hook" de Render, appelé par GitHub Actions après la publication de l'image Docker.

--------------------------------------------
PostgreSQL
--------------------------------------------
J'ai gardé SQLite pour le développement local. En revanche, en production, Django utilise PostgreSQL lorsque la variable ``DATABASE_URL`` est renseignée. La configuration se trouve dans ``oc_lettings_site/settings.py`` et utilise ``dj-database-url``. Les migrations Django permettent de créer et de mettre à jour les tables. Il faut aussi savoir que les migrations ne transfèrent pas automatiquement les données de la base SQLite locale vers PostgreSQL.

--------------------------------------------
Sentry
--------------------------------------------
Ici, Sentry est utilisé pour surveiller les erreurs de l'application. Sentry permet de consulter l'historique des erreurs enregistrées depuis son tableau de bord.

Son initialisation se trouve dans ``oc_lettings_site/settings.py``.

La connexion utilise la variable d'environnement ``SENTRY_DSN``, sans enregistrer le DSN directement dans le code.

--------------------------------------------
Logging
--------------------------------------------
Le logging est configuré dans ``oc_lettings_site/settings.py`` avec le module ``logging`` de Python.

Deux niveaux sont utilisés :

* ``INFO`` : avec le suivi des consultations de locations dans ``lettings/views.py``.
* ``ERROR`` : la journalisation des erreurs HTTP importantes via ``django.request``.

Les messages sont envoyés vers la console du serveur.

--------------------------------------------
Concernant la maintenance
--------------------------------------------
Les modifications du projet sont vérifiées par les tests et les contrôles de qualité du pipeline CI/CD. Lorsqu'un push est effectué sur ``master``, une nouvelle image Docker est publiée si les vérifications réussissent. Ensuite, le déploiement est déclenché automatiquement sur Render. Enfin, dans le même temps, les erreurs peuvent être suivies depuis Sentry et les journaux du service Render.