# *ORANGE COUNTY LETTINGS*

**Projet 13 — OpenClassrooms**  
**Réfactorisation effectuée par Marion LARUE**

**Lien GitHub :** https://github.com/mrnlarue-cloud/Python-OC-Lettings-FR

## *Présentation*

Il s'agit ici d'une application Django de consultation de locations immobilières et de profils utilisateurs dans le comté d'Orange, aux États-Unis. La réfactorisation a été faite de manière modulaire avec un déploiement automatisé.

## *Architecture*

```text
Python-OC-Lettings-FR/
├── oc_lettings_site/         # Configuration et accueil
├── lettings/                # Adresses et locations
├── profiles/                # Profils utilisateurs
├── templates/               # Templates communs
├── static/                  # Fichiers statiques
├── docs/source/             # Documentation Sphinx
├── .github/workflows/ci.yml # Pipeline CI/CD
├── Dockerfile
├── .env.exemple
├── manage.py
├── requirements.txt
└── README.md
```

Les applications `lettings` et `profiles` possèdent leurs propres vues, modèles et tests. L'application `oc_lettings_site` gère la configuration et l'accueil du site. C'est un projet qui utilise SQLite en local et PostgreSQL en production.

## *Concernant l'installation et le démarrage*

**Les prérequis :** Python 3.11 ainsi que Git.

```powershell
git clone https://github.com/mrnlarue-cloud/Python-OC-Lettings-FR.git
cd Python-OC-Lettings-FR
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Sur Linux/macOS, activer l'environnement avec `source .venv/bin/activate`.

Créer un fichier `.env` à partir de `.env.exemple` et renseigner la clé secrète Django.

```powershell
python manage.py migrate
python manage.py runserver
```

**Site :** http://localhost:8000/

## *Concernant l'administration et la base de données*

**Administration :** http://localhost:8000/admin/

Identifiants de démonstration locale initiaux :

- Utilisateur : `admin`
- Mot de passe : `Abc1234!`

Attention : ne pas utiliser ces identifiants en production.

Pour consulter les tables SQLite : `sqlite3 oc-lettings-site.sqlite3`, puis `.tables`.

## *Concernant les tests et la qualité du code*

```powershell
python -m pytest
python -m flake8 --config=setup.cfg . --extend-exclude=.venv
```

Pour ce projet, une couverture de tests supérieure à 80 % était exigée et c'est bien le cas ici.

## *Concernant le déploiement*

**GitHub → GitHub Actions → Docker Hub → Render**

GitHub Actions exécute les tests ainsi que Flake8. Après validation sur `master`, une image Docker est publiée et le déploiement Render se déclenche.

Pour reproduire ce déploiement :

1. Configurer la variable GitHub `DOCKERHUB_USERNAME` et les secrets `DOCKERHUB_TOKEN` et `RENDER_DEPLOY_HOOK`.
2. Créer une base PostgreSQL et un service web Render utilisant l'image `marionlarue/oc-lettings:latest`.
3. Configurer sur Render : `DJANGO_SECRET_KEY`, `DJANGO_DEBUG=False`, `DJANGO_ALLOWED_HOSTS`, `DATABASE_URL` et `SENTRY_DSN`.
4. Enfin, il faut appliquer les migrations Django sur PostgreSQL et configurer le Deploy Hook dans GitHub.

Relativement à la récupération de l'image Docker :

```powershell
docker pull marionlarue/oc-lettings:latest
```

**Pipeline :** https://github.com/mrnlarue-cloud/Python-OC-Lettings-FR/actions

## *Concernant la documentation*

La documentation Sphinx vient détailler toute l'installation, l'architecture, le déploiement et la surveillance grâce à Sentry.

**Read the Docs :**