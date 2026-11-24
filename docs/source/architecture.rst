========================
Mon architecture Django
========================

------------------------------------------
L'organisation de mon projet
------------------------------------------

Pour la réfactorisation de ce projet, je suis partie sur une logique "Fat Models", "Skinny Views" et une architecture modulaire. Le principe était de pouvoir garder la logique métier avec les modèles et des vues simples.

J'ai donc divisé le projet en trois applications Django :

* ``oc_lettings_site`` : pour la configuration principale et la page d'accueil.
* ``lettings`` : concernant la gestion des adresses et des locations du site.
* ``profiles`` : concernant la gestion des profils utilisateurs.

------------------------------------------
Les modèles et la base de données
------------------------------------------

Ce projet utilise trois modèles principaux :

* ``Address`` : pour les informations relatives aux adresses.
* ``Letting`` : pour les locations immobilières avec leurs adresses respectives.
* ``Profile`` : pour les différents profils utilisateurs avec leur ville favorite.

Les modèles ``Address`` et ``Letting`` se trouvent dans ``lettings/models.py``, alors que ``Profile`` est, lui, défini dans ``profiles/models.py``.

Chaque location est associée à une adresse avec une relation ``OneToOneField``. Enfin, chaque profil est lié à un utilisateur Django.

Ici, c'est SQLite qui est utilisé en local et PostgreSQL pour la partie production.