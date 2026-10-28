from django.urls import path
from . import views

urlpatterns = [
    path("", views.accueil, name="accueil"),
    path("a-propos/", views.a_propos, name="a_propos"),
    path("produits/", views.produits, name="produits"),
    path("projets/", views.projets, name="projets"),
    path("contact/", views.contact, name="contact"),
]
