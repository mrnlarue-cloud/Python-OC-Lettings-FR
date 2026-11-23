======================
ORANGE COUNTY LETTINGS
======================

------------------------------------------
Présentation du projet OC Lettings
------------------------------------------

L'application Orange County Lettings est une application web qui est développée avec Django ; elle permet de consulter certaines locations immobilières, mais aussi les profils des utilisateurs inscrits.

Cette application nous propose une page d'accueil, la liste des locations disponibles et les profils des personnes inscrites. L'application est composée de pages avec les différents détails relatifs aux locations et aux profils ainsi qu'une interface pour le profil administrateur.

------------------------------------------
Architecture du projet
------------------------------------------

Pour ce projet, nous avons trois applications Django :

* ``oc_lettings_site`` : Cette application gère la page d'accueil et la configuration principale.
* ``lettings`` : ici, il s'agit de la gestion des adresses relatives aux locations immobilières.
* ``profiles`` : enfin, cette application gère la partie des profils utilisateurs.

------------------------------------------
Objectifs de cette documentation
------------------------------------------

La documentation technique vient représenter les phases d'installation, de configuration, d'architecture et de fonctionnement de l'application ORANGE COUNTY LETTINGS.

Elle permet de même d'expliquer les procédures de test, du déploiement et de la maintenance de ce projet.

.. toctree::
   :maxdepth: 2
   :caption: Sommaire