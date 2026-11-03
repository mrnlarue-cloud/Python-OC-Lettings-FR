"""Configuration générale du projet Django OC Lettings."""

import os
from pathlib import Path
from dotenv import load_dotenv
import sentry_sdk

# ==================================================
# CHEMINS DU PROJET
# ==================================================

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

# ==================================================
# SURVEILLANCE DES ERREURS - SENTRY
# ==================================================

# Limite les données personnelles envoyées à Sentry avec les erreurs
sentry_sdk.init(
    dsn=os.getenv("SENTRY_DSN"),
    data_collection={
        "user_info": False,
        "http_bodies": [],
    },
)

# ==================================================
# SECURITE ET ENVIRONNEMENT
# ==================================================

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ["DJANGO_SECRET_KEY"]

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv("DJANGO_DEBUG", "False").lower() == "true"
ALLOWED_HOSTS = [
    host.strip()
    for host in os.getenv("DJANGO_ALLOWED_HOSTS", "localhost,127.0.0.1").split(",")
    if host.strip()
]

# ==================================================
# APPLICATIONS INSTALLEES
# ==================================================

INSTALLED_APPS = [
    "oc_lettings_site.apps.OCLettingsSiteConfig",
    "lettings.apps.LettingsConfig",
    "profiles.apps.ProfilesConfig",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

# ==================================================
# MIDDLEWARES
# ==================================================

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# ==================================================
# ROUTAGE ET TEMPLATES
# ==================================================

ROOT_URLCONF = "oc_lettings_site.urls"
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]
WSGI_APPLICATION = "oc_lettings_site.wsgi.application"

# ==================================================
# BASE DE DONNEES
# ==================================================

# https://docs.djangoproject.com/en/5.2/ref/settings/#databases
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "oc-lettings-site.sqlite3"),
    }
}

# ==================================================
# VALIDATION DES MOTS DE PASSE
# ==================================================

# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# ==================================================
# INTERNATIONALISATION
# ==================================================

# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# ==================================================
# FICHIERS STATIQUES
# ==================================================

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATIC_URL = "/static/"
STATICFILES_DIRS = [
    BASE_DIR / "static",
]

# ==================================================
# JOURNALISATION DES ERREURS
# ==================================================

# Affiche les erreurs HTTP importantes dans le terminal
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
        },
    },
    "loggers": {
        "django.request": {
            "handlers": ["console"],
            "level": "ERROR",
            "propagate": False,
        },
    },
}

# ==================================================
# CONFIGURATION DES CLES PRIMAIRES
# ==================================================

DEFAULT_AUTO_FIELD = "django.db.models.AutoField"
