# Aciérie d'Haïti - Site Vitrine Django

Bienvenue sur le dépôt du projet **Aciérie d'Haïti**, un site web vitrine moderne développé avec le framework web [Django](https://www.djangoproject.com/). Ce projet présente les activités, l'histoire, les produits, les projets phares et les informations de contact de l'entreprise *Aciérie d'Haïti*, une référence dans le secteur métallurgique et les matériaux de construction en Haïti.

---

## 📌 Sommaire

- [À propos du projet](#-à-propos-du-projet)
- [Fonctionnalités](#-fonctionnalités)
- [Technologies utilisées](#-technologies-utilisées)
- [Structure du projet](#-structure-du-projet)
- [Prérequis](#-prérequis)
- [Installation et Configuration](#-installation-et-configuration)
- [Lancement de l'application](#-lancement-de-lapplication)
- [Auteur et Contribution](#-auteur-et-contribution)

---

## 📖 À propos du projet

Fondée au début des années 1970, **Aciérie d'Haïti** est une entreprise pionnière dans la fourniture d'aciers de construction, barres d'armature, clous, fils d'attache et profilés structuraux.

Ce projet vise à fournir une présence numérique moderne, réactive et élégante pour l'entreprise. Il permet aux clients, entrepreneurs et partenaires de découvrir l'histoire de la compagnie, d'explorer le catalogue de produits, de consulter les projets réalisés et de solliciter des devis ou informations via un formulaire de contact.

---

## 🎯 Fonctionnalités

Le site vitrine se compose de 5 pages principales accessibles via une navigation fluide :

1. **Accueil (`/`)** : Présentation générale de l'entreprise, mise en avant des produits vedettes et des services.
2. **À propos (`/a-propos/`)** : Histoire de l'entreprise (chronologie depuis 1972), mission, vision et valeurs.
3. **Produits (`/produits/`)** : Catalogue des matériaux de construction métalliques (aciers, barres d'armature, clous, tôle, etc.).
4. **Projets (`/projets/`)** : Galerie et descriptifs des réalisations majeures soutenues par l'entreprise (résidentiel, commercial, industriel).
5. **Contact (`/contact/`)** : Formulaire de contact, coordonnées géographiques et horaires d'ouverture.

---

## 🛠️ Technologies utilisées

- **Backend** : Python 3.x, Django 5.2.x
- **Frontend** : HTML5, CSS3, JavaScript (ES6+), [Bootstrap 5.3](https://getbootstrap.com/), [Bootstrap Icons](https://icons.getbootstrap.com/)
- **Gestion des dépendances** : `pip` / `requirements.txt`

---

## 📁 Structure du projet

```
acierie-haiti-django/
├── config/                  # Configuration globale du projet Django
│   ├── __init__.py
│   ├── asgi.py              # Entrée ASGI pour le déploiement
│   ├── settings.py          # Paramètres du projet Django
│   ├── urls.py              # Routage principal
│   └── wsgi.py              # Entrée WSGI pour le déploiement
├── vitrine/                 # Application Django "vitrine"
│   ├── migrations/          # Migrations de base de données
│   ├── admin.py
│   ├── apps.py
│   ├── models.py            # Modèles de données (extensible)
│   ├── tests.py             # Tests unitaires
│   ├── urls.py              # Routage des URLs de la vitrine
│   └── views.py             # Contrôleurs / vues
├── templates/               # Gabarits HTML Django
│   ├── base.html            # Template de base (en-tête, navigation, pied de page)
│   ├── index.html           # Page d'accueil
│   ├── a-propos.html        # Page À propos
│   ├── produits.html        # Page Produits
│   ├── projets.html         # Page Projets
│   └── contact.html         # Page Contact
├── static/                  # Fichiers statiques
│   ├── css/                 # Feuilles de style (style.css)
│   ├── images/              # Images du site (timeline, etc.)
│   └── js/                  # Scripts JavaScript (script.js)
├── manage.py                # Script de commande Django
├── requirements.txt         # Dépendances du projet
└── README.md                # Documentation du projet
```

---

## 📋 Prérequis

Avant de commencer, assurez-vous de disposer des éléments suivants sur votre machine :

- **Python** 3.10 ou supérieur
- **pip** (gestionnaire de paquets Python)
- **venv** (recommandé pour l'isolation des dépendances)

---

## 🚀 Installation et Configuration

1. **Cloner le dépôt Git :**

   ```bash
   git clone https://github.com/ednor/acierie-haiti-django.git
   cd acierie-haiti-django
   ```

2. **Créer et activer un environnement virtuel :**

   - Sur Linux / macOS :
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```
   - Sur Windows (PowerShell) :
     ```powershell
     python -m venv venv
     .\venv\Scripts\Activate.ps1
     ```

3. **Installer les dépendances :**

   ```bash
   pip install -r requirements.txt
   ```

4. **Appliquer les migrations (si nécessaire) :**

   ```bash
   python manage.py migrate
   ```

---

## 💻 Lancement de l'application

Pour exécuter le serveur de développement local :

```bash
python manage.py runserver
```

Le site sera ensuite accessible sur votre navigateur à l'adresse suivante : [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

---

## 🧪 Exécution des tests

Pour lancer les tests unitaires de l'application :

```bash
python manage.py test
```

---

## 📜 Licence & Crédits

Projet développé pour **Aciérie d'Haïti**. Tous droits réservés.
