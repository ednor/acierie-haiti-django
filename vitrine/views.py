from django.shortcuts import render


def accueil(request):
    return render(request, "index.html")


def a_propos(request):
    return render(request, "a-propos.html")


def produits(request):
    return render(request, "produits.html")


def projets(request):
    return render(request, "projets.html")


def contact(request):
    return render(request, "contact.html")
