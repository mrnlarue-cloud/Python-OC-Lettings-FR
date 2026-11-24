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