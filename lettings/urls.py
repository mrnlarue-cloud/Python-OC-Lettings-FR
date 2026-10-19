"""Routes URL de l'application Lettings."""

from django.urls import path
from . import views

# ==================================================
# URL : LOCATIONS IMMOBILIÈRES (Lettings)
# ==================================================

app_name = "lettings"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:letting_id>/", views.letting, name="letting"),
]
