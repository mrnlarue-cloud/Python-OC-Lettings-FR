# ==================================================
# BASE AVEC PYTHON 3.11
# ==================================================
FROM python:3.11

# ==================================================
# REPERTOIRE DE TRAVAIL DU CONTENEUR
# ==================================================
WORKDIR /app

# ==================================================
# COPIE DU FICHIER DES DEPENDANCES
# ==================================================
COPY requirements.txt .

# ==================================================
# INSTALLATION AUTOMATIQUE DES DEPENDANCES
# ==================================================
RUN pip install --no-cache-dir -r requirements.txt

# ==================================================
# COPIE DU CODE DE L'APPLICATION
# ==================================================
COPY . .

# ==================================================
# PORT DJANGO
# ==================================================
EXPOSE 8000

# ==================================================
# DEMARRAGE DU SERVEUR DJANGO EN PRODUCTION
# ==================================================
CMD python manage.py collectstatic --noinput \
    && exec gunicorn oc_lettings_site.wsgi:application \
    --bind "0.0.0.0:${PORT:-8000}"