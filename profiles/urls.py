"""Routes URL de l'application Profiles."""

from django.urls import path
from . import views

# ==================================================
# URL : PROFILS UTILISATEURS (Profiles)
# ==================================================

app_name = "profiles"

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:username>/", views.profile, name="profile"),
]
