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

------------------------------------------
Les vues, les URL et les templates
------------------------------------------
Mes URL principales se trouvent dans ``oc_lettings_site/urls.py`` et les applications ``lettings`` et ``profiles`` possèdent leurs propres fichiers ``urls.py`` et ``views.py``.

Les routes principales du site sont :

* ``/`` : page d'accueil.
* ``/lettings/`` : liste des locations.
* ``/lettings/<int:letting_id>/`` : détail d'une location.
* ``/profiles/`` : liste des profils.
* ``/profiles/<str:username>/`` : détail d'un profil.
* ``/admin/`` : interface d'administration.

De leur côté, les templates sont répartis dans ces dossiers :

* ``templates/`` : accueil, base commune et pages d'erreur.
* ``lettings/templates/temp_lettings/`` : pages des locations.
* ``profiles/templates/temp_profiles/`` : pages des profils.

------------------------------------------
Petit guide d'utilisation
------------------------------------------
L'application permet de consulter les locations immobilières et les profils utilisateurs. Depuis la page d'accueil, deux boutons permettent d'accéder aux différentes listes.

Pour consulter une location, il suffit de cliquer sur "Lettings", puis de sélectionner une location dans la liste. Une nouvelle page affiche alors son nom et son adresse.

Pour consulter un profil utilisateur, le principe est le même. Il faut cliquer sur "Profiles", puis sélectionner un utilisateur pour afficher son nom et sa ville favorite.

Enfin, une interface d'administration Django est accessible depuis ``/admin/``. Elle permet aux utilisateurs autorisés de gérer les données de l'application.